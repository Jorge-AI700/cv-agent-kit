#!/usr/bin/env python3
"""Check a tailored CV against the private rules file and the master CV.

Checks:
  * banned terms from the rules file (ERROR, case-insensitive, whole word/phrase)
  * entry titles: each `### Title — Organisation` must use the real title recorded
    in the master for that organisation. A target-function suffix such as
    `Founder (Business Development)` is allowed, and so are title translations
    listed in the rules file (ERROR on mismatch, WARNING if the organisation is
    not in the master)
  * numbers, percentages and money not found in the master (WARNING)
  * basic renderer structure (ERROR)

Exit code is 1 when any ERROR is found, otherwise 0.
"""
import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^##+\s+(.+?)\s*$")
BULLET = re.compile(r"^\s*[-*]\s+")
DASH = re.compile(r"\s[—–]\s")
SUFFIX = re.compile(r"^(.*\S)\s*\(([^()]+)\)\s*$")
NUMBER = re.compile(r"(?<![\w.,])(?:[$€£]\s*)?\d+(?:[.,]\d+)*(?:\s*%|\s*(?:k|m|bn|million|billion))?(?![\w])", re.I)


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot read {path}: {exc}") from exc


def section_bullets(text, *keywords, any_of=()):
    """Bullet lines under any ## heading containing all keywords (and one of any_of)."""
    items, active = [], False
    for line in text.splitlines():
        heading = HEADING.match(line)
        if heading:
            label = heading.group(1).casefold()
            active = all(k in label for k in keywords) and (not any_of or any(w in label for w in any_of))
        elif active and BULLET.match(line):
            item = BULLET.sub("", line).strip().strip("`\"'")
            if item:
                items.append(item)
    return items


def banned_terms(rules):
    return section_bullets(rules, "banned", any_of=("word", "phrase", "term"))


def title_translations(rules):
    """`## Title translations` bullets: `Original title = Translated title`."""
    mapping = {}
    for item in section_bullets(rules, "translation"):
        if "=" in item:
            original, translated = (part.strip().strip("`") for part in item.split("=", 1))
            mapping[translated.casefold()] = original.casefold()
    return mapping


def check_banned(path, text, terms):
    hits = []
    for number, line in enumerate(text.splitlines(), 1):
        for term in terms:
            if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", line, re.I):
                hits.append(f"ERROR banned term {term!r}: {path}:{number}: {line.strip()}")
    return hits


def entries(text):
    """Yield (line_no, title, organisation) for `### Title — Organisation | ...` lines."""
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("### ") and DASH.search(line):
            title, rest = DASH.split(line[4:], maxsplit=1)
            yield number, title.strip(), rest.split("|")[0].strip()


def check_titles(path, cv, master, translations):
    known = {}
    for _, title, org in entries(master):
        known.setdefault(org.casefold(), {})[title.casefold()] = title
    errors, warnings = [], []
    for number, title, org in entries(cv):
        titles = known.get(org.casefold())
        if titles is None:
            warnings.append(f"WARNING organisation not in master {org!r}: {path}:{number}")
            continue
        candidates = [title]
        suffix = SUFFIX.match(title)
        if suffix:
            candidates.append(suffix.group(1))
        candidates = [c.casefold() for c in candidates]
        candidates += [translations[c] for c in candidates if c in translations]
        if not any(c in titles for c in candidates):
            real = " / ".join(sorted(titles.values()))
            errors.append(
                f"ERROR title {title!r} at {org!r} does not match the master ({real}); "
                f"keep the real title and add the target function in brackets: {path}:{number}"
            )
    return errors, warnings


def norm_number(value):
    """Normalise common English/European thousands separators for comparison."""
    value = re.sub(r"\s+", "", value).casefold()
    match = re.search(r"\d+(?:[.,]\d+)*", value)
    if not match:
        return value
    number = match.group()
    if number.count(",") + number.count(".") == 1 and re.search(r"[,.]\d{3}$", number):
        number = number.replace(",", "").replace(".", "")
    elif "," in number and "." not in number:
        number = number.replace(",", ".")
    return value[:match.start()] + number + value[match.end():]


def structure_errors(path, text):
    lines, errors = text.splitlines(), []
    if not any(re.match(r"^#\s+\S", line) for line in lines):
        errors.append(f"ERROR structure: {path} has no '# Name' heading")
    if not any(re.match(r"^##\s+\S", line) for line in lines):
        errors.append(f"ERROR structure: {path} has no '##' section")
    items = [line for line in lines if line.startswith("### ")]
    if not items:
        errors.append(f"ERROR structure: {path} has no '###' entries")
    for line in items:
        if not DASH.search(line):
            errors.append(f"ERROR structure: entry needs a spaced em/en dash: {line}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cv", type=Path, help="tailored cv.md")
    parser.add_argument("--rules", required=True, type=Path, help="private rules file")
    parser.add_argument("--master", required=True, type=Path, help="master CV")
    parser.add_argument("--extra-text", action="append", default=[], type=Path,
                        help="other text to scan for banned terms and numbers (answers, cover letter)")
    args = parser.parse_args()
    cv, rules, master = read(args.cv), read(args.rules), read(args.master)
    terms = banned_terms(rules)
    errors = structure_errors(args.cv, cv)
    title_errors, warnings = check_titles(args.cv, cv, master, title_translations(rules))
    errors += title_errors
    checked = [(args.cv, cv)] + [(path, read(path)) for path in args.extra_text]
    for path, text in checked:
        errors += check_banned(path, text, terms)
    known = {norm_number(m.group()) for m in NUMBER.finditer(master + "\n" + rules)}
    for path, text in checked:
        for line_no, line in enumerate(text.splitlines(), 1):
            seen = set()
            for match in NUMBER.finditer(line):
                token = norm_number(match.group())
                if token not in known and token not in seen:
                    seen.add(token)
                    warnings.append(f"WARNING untraceable number {match.group()!r}: {path}:{line_no}: {line.strip()}")
    print(f"Banned terms loaded: {len(terms)}")
    for message in errors + warnings:
        print(message)
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

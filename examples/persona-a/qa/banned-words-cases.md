# Banned-word QA cases (fictional)

Pass this file to `qa_check.py` with `--extra-text`. Every row except the last should be reported as a banned term. The last row must **not** be reported, because matching uses whole words.

See “Running the checks” in [examples/README.md](../../README.md) for the command.

| Phrase | Why it is banned | Replacement |
| --- | --- | --- |
| gave a demo to a workshop | the user prefers "pilot"; "demo" undersells real use | onboarded a pilot workshop |
| EU citizen | untrue work-authorisation claim | ASK USER |
| unrestricted right to work | unconfirmed legal claim | ASK USER |
| expert in SQL | inflated skill level | SQL (basic) |
| passionate rockstar | generic filler | a proof point |
| results-driven coordinator | generic filler | a measured result |
| founded BiciCita | old working name | RutaTaller |
| analysed demographics | false-positive guard: the banned word appears only inside a longer word | keep unchanged |

Invented percentages are not a banned word but a number check: an answer saying "cut costs by 47%" produces `WARNING untraceable number '47%'` because 47% is not in the master or rules.

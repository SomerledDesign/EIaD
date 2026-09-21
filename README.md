# EIaD — English Idiom a Day

Small Python CLI that picks a random British / English idiom from a built-in dictionary and emails it (Gmail SMTP) to one address or a list.

Repo name is **EIaD** (capital **i**). Sibling spirit to [WaD](https://github.com/SomerledDesign/WaD) (Word a Day).

## Dictionary

`EIaDDictionary.py` exports a single `dictionary` map: idiom → explanation (often with a short origin note and an example).

Roughly ninety entries at last count — enough for a few months of daily sends without repeats if you track history externally.

## Requirements

- Python 3
- A Gmail (or Gmail-compatible) account that can send via SMTP on port 587 (app password recommended)

Stdlib only — no pip dependencies.

## Usage

```bash
./eiad.py -u you@gmail.com -p 'app-password' -e friend@example.com
```

| Flag | Meaning |
| --- | --- |
| `-u` / `--user` | From address (required) |
| `-p` / `--password` | SMTP password (required) |
| `-e` / `--email` | Single recipient |
| `-f` / `--file` | File of recipient addresses (one per line) |
| `-n` / `--name` | Display name in the From header |
| `-V` / `--version` | Print version |

If neither `-e` nor `-f` is given, placeholder recipients in the script are used — edit those before a bare run.

## Layout

| File | Role |
| --- | --- |
| `eiad.py` | CLI entry |
| `EIaDDictionary.py` | Idiom dictionary |
| `alert.py` | Gmail SMTP send helper |

## Notes

- Subject is the idiom; body is the definition / colour.
- Same SMTP caveats as WaD: keep passwords out of cron command lines when you can.
- `.gitignore` excludes venv noise and `email_list.txt`.

## License

Public Somerled Design project on GitHub unless noted otherwise.

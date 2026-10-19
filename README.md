# DocuMind

Multi-tenant AI document Q&A API. Upload documents, ask questions, get answers grounded in your own files.

> Status: project scaffold. The API, database, and AI features are added week by week.

## Prerequisites

- Python 3.12+
- Git

## Setup (Windows PowerShell)

```powershell
git clone https://github.com/dil-Sumukh/documind.git
cd documind
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env   # then fill in values
python -m app.main
```

On macOS/Linux or Git Bash, activate with `source .venv/bin/activate` (Git Bash: `source .venv/Scripts/activate`) and copy with `cp .env.example .env`.

Expected output:

```text
DocuMind starting in production mode
```

## Configuration

All settings are read from environment variables (loaded from `.env`) by `app/config.py`. The app refuses to start if any required variable is missing and lists every missing one at once.

| Variable       | Description                                  | Example                                                        |
| -------------- | -------------------------------------------- | -------------------------------------------------------------- |
| `APP_NAME`     | Display name of the application              | `DocuMind`                                                     |
| `DEBUG`        | Debug mode (`true`/`1`/`yes` to enable)      | `false`                                                        |
| `DATABASE_URL` | SQLAlchemy-style Postgres connection string  | `postgresql+psycopg://USER:PASSWORD@localhost:5432/documind`   |

Never commit `.env`. It is listed in `.gitignore`; only `.env.example` is tracked.

## Project layout

```text
documind/
├── app/
│   ├── __init__.py
│   ├── config.py      # settings loader, fails loudly on missing vars
│   └── main.py        # entry point: python -m app.main
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

Run the app as a module from the repo root (`python -m app.main`), not as a script (`python app/main.py`), so `app` imports resolve.

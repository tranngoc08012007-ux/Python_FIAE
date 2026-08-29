# Lesson 03 — Code Quality Tools (Black & Flake8)

## Objective

Learn how to maintain clean, consistent, and professional Python code
by using code quality tools — a standard practice in German Betrieb environments.

---

## Topics Covered

- Install **Black** (Python code formatter)
- Install **Flake8** (Python linter)
- Configure **.editorconfig**
- Configure **.flake8**
- Enable **Format on Save** in VS Code
- Understand the difference between a formatter and a linter

---

## Formatter vs Linter

| | Black | Flake8 |
|---|---|---|
| Type | Formatter | Linter |
| Action | Auto-fixes code style | Reports issues only |
| Fixes | Spacing, indentation, line length | Unused imports, undefined variables, style violations |
| Run order | Run first | Run after Black |

---

## Project Structure

```
Lesson_03_Code_Quality/
│
├── main.py
├── README.md
├── .editorconfig
├── .flake8
├── requirements-dev.txt
└── .gitignore
```

---

## Development Tools

- Python 3.11
- VS Code
- Black
- Flake8

---

## Editor Configuration

This project uses `.editorconfig` to enforce consistent formatting rules
(indentation, line endings, charset) across different editors and IDEs.

---

## Run

```bash
python main.py
```

## Format Code

```bash
black .
```

## Check Code Quality

```bash
flake8 .
```

## Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

---

## What I Learned

- The difference between a formatter (Black) and a linter (Flake8)
- How Black automatically formats Python code to PEP 8 style
- How Flake8 detects issues that Black cannot fix (unused imports, undefined variables)
- How to configure `.flake8` to sync with Black and exclude `.venv`
- How to configure `.editorconfig` for consistent editor behavior
- How to use `requirements-dev.txt` to separate dev dependencies

---

## Author

Tran Nguyen Ngoc
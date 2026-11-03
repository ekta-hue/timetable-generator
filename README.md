# Examination Timetable Generator (PS No. 92)

## Project Overview
A console program in Python 3 that generates an exam date sheet from a list of
subjects, a start date and optional holidays. Exactly one exam is scheduled per
day, in the order the subjects are given. Sundays and holidays are skipped.

## Objectives
- Understand the problem and define it clearly.
- Apply lists, dictionaries, scheduling logic and constraints.
- Use the `datetime` module to find dates and weekday names.
- Validate user input and report clear error messages.

## Features
- Accepts comma-separated subjects, a start date (`DD-MM-YYYY`) and optional holidays.
- Validates input: date format, empty subject list, duplicate subjects.
- Schedules one exam per day in the given order.
- Skips Sundays and holiday dates automatically (also when the start date itself is one).
- Prints each entry as `Subject : DD-MM-YYYY (Weekday)`.
- Built-in `--test` mode that runs all four test cases.

## Requirements
- Python 3.6 or later
- No external libraries (uses only `sys` and `datetime` from the standard library)

## How It Works
1. **Validation** – `validate_subjects`, `parse_date` and `validate_holidays` check the input.
   `parse_date` enforces the strict `DD-MM-YYYY` shape and rejects impossible dates such as `32-10-2026`.
2. **Scheduling** – `generate_timetable` starts at the start date. For each subject it moves forward
   while the current day is a Sunday (`weekday() == 6`) or a holiday, assigns the subject, then moves to the next day.
3. **Data structures** – subjects and holidays are held in **lists**; each date-sheet entry is a
   **dictionary** `{"subject": ..., "date": ..., "day": ...}` stored in a list.
4. **Output** – `format_entry` prints each dictionary in the required format.

## Execution Instructions
Interactive mode:
```
python one.py
```
You will be asked for:
```
Subjects (comma separated): DAA, DBMS, OOP, Maths, CSA
Start date (DD-MM-YYYY): 12-10-2026
Holidays (DD-MM-YYYY, comma separated, or 'none'): 14-10-2026
```
Run all four test cases:
```
python one.py --test
```

## Input / Output Details
| Input | Format |
|---|---|
| Subjects | Comma-separated names, e.g. `DAA, DBMS, OOP` (no duplicates, at least one) |
| Start date | `DD-MM-YYYY` |
| Holidays | Comma-separated `DD-MM-YYYY` dates, or `none` |

Output: one line per subject, `Subject : DD-MM-YYYY (Weekday)`.

Error messages:
- `Invalid date. Please enter the date as DD-MM-YYYY.`
- `At least one subject is required.`
- `Duplicate subject: <name>`

## Test Cases
| # | Input | Expected output |
|---|---|---|
| 1 Normal | DAA, DBMS, OOP, Maths, CSA; 12-10-2026; holiday 14-10-2026 | DAA 12-10 Mon, DBMS 13-10 Tue, OOP 15-10 Thu, Maths 16-10 Fri, CSA 17-10 Sat |
| 2 Boundary | DAA; 18-10-2026 (Sunday); none | DAA : 19-10-2026 (Monday) |
| 3 Invalid | (a) date 32-10-2026 (b) no subjects (c) DAA, DAA | the three error messages above |
| 4 Different valid | DAA, DBMS, OOP, Maths, CSA, DM, Java; 12-10-2026; none | ... DM 17-10 Sat, Java 19-10 Mon (Sunday 18-10 skipped) |

All four cases pass (see `python one.py --test`). Screenshots of every case are in
`screenshots.pdf`.

## Files
- `one.py` – complete program
- `README.md` – this documentation
- `screenshots.pdf` – input/output screenshots for each test case

## Author
Project submitted for PS No. 92 – Examination Timetable Generator.

"""
PS 92 - Examination Timetable Generator
Language : Python 3
Concepts : Lists, Dictionaries, Scheduling, Constraints
"""

from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"          # DD-MM-YYYY
DATE_ERROR = "Invalid date. Please enter the date as DD-MM-YYYY."


# STEP 1: PARSING (turn typed text into Python data)
def parse_subjects(text):
    """'DAA, DBMS , OOP' -> ['DAA', 'DBMS', 'OOP']"""
    subjects = []
    for part in text.split(","):
        name = part.strip()
        if name and name.lower() != "none":
            subjects.append(name)
    return subjects


def parse_date(text):
    """Convert 'DD-MM-YYYY' into a date. Returns None if invalid."""
    try:
        return datetime.strptime(text.strip(), DATE_FORMAT).date()
    except ValueError:
        return None


# STEP 2: VALIDATION
def validate(subjects, start_text, holiday_text):
    """Return (errors, start_date, holidays)."""
    errors = []

    # At least one subject
    if len(subjects) == 0:
        errors.append("At least one subject is required.")

    # No duplicate subjects (case-insensitive)
    seen = set()
    for name in subjects:
        key = name.lower()
        if key in seen:
            errors.append(f"Duplicate subject: {name}.")
            break
        seen.add(key)

    # Valid start date
    start_date = parse_date(start_text)
    if start_date is None:
        errors.append(DATE_ERROR)

    # Valid holidays (optional)
    holidays = set()
    if holiday_text.strip() and holiday_text.strip().lower() != "none":
        for piece in holiday_text.split(","):
            d = parse_date(piece)
            if d is None:
                if DATE_ERROR not in errors:
                    errors.append(DATE_ERROR)
            else:
                holidays.add(d)

    return errors, start_date, holidays


# STEP 3: SCHEDULING
def generate_timetable(subjects, start_date, holidays):
    """One exam per day, skipping Sundays and holidays."""
    timetable = []
    current = start_date

    for subject in subjects:
        while current.weekday() == 6 or current in holidays:   # 6 = Sunday
            current += timedelta(days=1)

        timetable.append({
            "subject": subject,
            "date": current,
            "day": current.strftime("%A"),
        })
        current += timedelta(days=1)

    return timetable


def print_timetable(timetable):
    print("\nExamination Timetable")
    print("-" * 30)
    for entry in timetable:
        print(f"{entry['subject']} : {entry['date'].strftime(DATE_FORMAT)} ({entry['day']})")


# STEP 4: RUN
def run(subject_text, start_text, holiday_text):
    subjects = parse_subjects(subject_text)
    errors, start_date, holidays = validate(subjects, start_text, holiday_text)

    if errors:
        for message in errors:
            print(message)
        return False

    print_timetable(generate_timetable(subjects, start_date, holidays))
    return True


def main():
    print("=== Examination Timetable Generator ===")
    subject_text = input("Subjects (comma separated): ")
    start_text = input("Start date (DD-MM-YYYY): ")
    holiday_text = input("Holidays (DD-MM-YYYY, comma separated, or 'none'): ")
    run(subject_text, start_text, holiday_text)


if __name__ == "__main__":
    main()
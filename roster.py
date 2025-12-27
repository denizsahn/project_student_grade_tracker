def load_students(path: str) -> list:
    import json
    try:
        with open(path, "r") as f:
            return json.load(f)  # Load student list
    except FileNotFoundError:
        return []  # Return empty list if file missing


def save_students(path: str, students: list) -> None:
    import json
    with open(path, "w") as f:
        json.dump(students, f, indent=2)  # Save students to disk


def add_student(students: list, student_data: dict) -> dict:
    students.append(student_data)  # Add student dictionary
    return student_data


def update_student(students: list, student_id: str, updates: dict) -> dict:
    for student in students:
        if student["id"] == student_id:
            student.update(updates)  # Update fields
            return student
    raise ValueError("Student not found")


def enroll_student(course_roster: dict, student_id: str) -> dict:
    course_roster.setdefault("students", [])
    if student_id not in course_roster["students"]:
        course_roster["students"].append(student_id)  # Enroll student
    return course_roster


def withdraw_student(course_roster: dict, student_id: str) -> dict:
    if student_id in course_roster.get("students", []):
        course_roster["students"].remove(student_id)  # Remove student
    return course_roster

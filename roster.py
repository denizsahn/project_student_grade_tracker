# roster.py – student and course management

import uuid  # uuid gives unique IDs for each student

def load_students(path):
    # This normally loads JSON, but kept simple for beginner template
    return []

def save_students(path, students):
    # Would save to JSON here
    pass

def add_student(students, student_data):
    # Assign a new ID to the student
    new_student = {
        "id": str(uuid.uuid4()),      # student ID
        "name": student_data["name"], # student name
        "email": student_data["email"]
    }
    students.append(new_student)
    return new_student

def update_student(students, student_id, updates):
    # Loop through students until ID matches
    for s in students:
        if s["id"] == student_id:
            s.update(updates)
            return s
    return None

def enroll_student(course_roster, student_id):
    # Add student to course list if not present
    if student_id not in course_roster["students"]:
        course_roster["students"].append(student_id)
    return course_roster

def withdraw_student(course_roster, student_id):
    # Remove student from course
    if student_id in course_roster["students"]:
        course_roster["students"].remove(student_id)
    return course_roster

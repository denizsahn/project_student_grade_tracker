import json
import uuid

def load_students(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_students(path, students):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

def add_student(students, student_data):
    # id otomatik olsun...
    new_student = {
        "id": str(uuid.uuid4()),
        "name": student_data.get("name"),
        "email": student_data.get("email")
    }
    students.append(new_student)
    return new_student

def update_student(students, student_id, updates):
    for s in students:
        if s["id"] == student_id:
            if "name" in updates:
                s["name"] = updates["name"]
            if "email" in updates:
                s["email"] = updates["email"]
            return s
    return None


# kurs işlemleri
def load_courses(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_courses(path, courses):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(courses, f, indent=2)

def add_course(courses, course_data):
    new_course = {
        "id": str(uuid.uuid4()),
        "code": course_data.get("code"),
        "title": course_data.get("title"),
        "term": course_data.get("term"),
        "roster": []
    }
    courses.append(new_course)
    return new_course

def enroll_student(course, student_id):
    if student_id not in course["roster"]:
        course["roster"].append(student_id)
    return course

def withdraw_student(course, student_id):
    if student_id in course["roster"]:
        course["roster"].remove(student_id)
    return course

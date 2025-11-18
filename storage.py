# json dosyalarını yüklemek ve kaydetmek için basit fonksiyonlar

import os
from roster import load_students, load_courses, save_students, save_courses

def load_state(base_dir):
    students = load_students(os.path.join(base_dir, "data", "students.json"))
    courses = load_courses(os.path.join(base_dir, "data", "courses.json"))
    return students, courses

def save_state(base_dir, students, courses):
    save_students(os.path.join(base_dir, "data", "students.json"), students)
    save_courses(os.path.join(base_dir, "data", "courses.json"), courses)

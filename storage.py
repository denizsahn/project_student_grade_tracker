import json
import os
import shutil
from datetime import datetime


def load_state(base_dir: str):
    # Ensure data directory exists
    os.makedirs(base_dir, exist_ok=True)

    # Helper function to load JSON safely
    def load_json(path, default):
        if not os.path.exists(path):
            return default  # Return empty structure if file doesn't exist
        with open(path, "r") as f:
            return json.load(f)  # Load JSON data

    students = load_json(os.path.join(base_dir, "students.json"), [])
    courses = load_json(os.path.join(base_dir, "courses.json"), [])
    gradebook = load_json(os.path.join(base_dir, "grades.json"), {})
    settings = load_json(os.path.join(base_dir, "settings.json"), {})

    return students, courses, gradebook, settings  # Return all system state


def save_state(base_dir: str, students: list, courses: list, gradebook: dict, settings: dict):
    os.makedirs(base_dir, exist_ok=True)

    # Save each component into its own JSON file
    with open(os.path.join(base_dir, "students.json"), "w") as f:
        json.dump(students, f, indent=2)

    with open(os.path.join(base_dir, "courses.json"), "w") as f:
        json.dump(courses, f, indent=2)

    with open(os.path.join(base_dir, "grades.json"), "w") as f:
        json.dump(gradebook, f, indent=2)

    with open(os.path.join(base_dir, "settings.json"), "w") as f:
        json.dump(settings, f, indent=2)


def backup_state(base_dir: str, backup_dir: str):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

    shutil.copytree(base_dir, backup_path)  # Copy all data files
    return [backup_path]  # Return created backup paths


def import_from_csv(csv_path: str, course_id: str):
    import csv
    gradebook = {}

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_id = row["student_id"]
            assessment_id = row["assessment_id"]

            gradebook.setdefault(course_id, {})
            gradebook[course_id].setdefault(student_id, {})
            gradebook[course_id][student_id][assessment_id] = {
                "score": float(row["score"]),
                "weight": float(row["weight"])
            }

    return gradebook  # Return imported grades


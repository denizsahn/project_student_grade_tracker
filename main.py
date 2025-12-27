from storage import load_state, save_state
from roster import add_student
from grades import record_grade

DATA_DIR = "data"


def main():
    students, courses, gradebook, settings = load_state(DATA_DIR)

    # Simple demo workflow
    student = {"id": "S001", "name": "Alice", "email": "alice@school.edu"}
    add_student(students, student)

    assessment = {
        "id": "A1",
        "name": "Midterm",
        "score": 85,
        "weight": 100
    }

    record_grade(gradebook, "CS101", "S001", assessment)

    save_state(DATA_DIR, students, courses, gradebook, settings)
    print("System state saved successfully.")


if __name__ == "__main__":
    main()


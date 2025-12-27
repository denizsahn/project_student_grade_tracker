def record_grade(gradebook: dict, course_id: str, student_id: str, assessment: dict) -> dict:
    gradebook.setdefault(course_id, {})
    gradebook[course_id].setdefault(student_id, {})

    assessment_id = assessment["id"]
    if assessment_id in gradebook[course_id][student_id]:
        raise ValueError("Duplicate assessment ID")

    if not 0 <= assessment["score"] <= 100:
        raise ValueError("Score must be between 0 and 100")

    gradebook[course_id][student_id][assessment_id] = assessment
    return gradebook


def update_grade(gradebook: dict, course_id: str, student_id: str, assessment_id: str, new_score: float) -> dict:
    if not 0 <= new_score <= 100:
        raise ValueError("Invalid score")

    gradebook[course_id][student_id][assessment_id]["score"] = new_score
    return gradebook


def delete_grade(gradebook: dict, course_id: str, student_id: str, assessment_id: str) -> dict:
    del gradebook[course_id][student_id][assessment_id]
    return gradebook


def calculate_student_average(gradebook: dict, course_id: str, student_id: str) -> float:
    scores = gradebook.get(course_id, {}).get(student_id, {}).values()
    if not scores:
        return 0.0

    total_weight = sum(a["weight"] for a in scores)
    if total_weight != 100:
        raise ValueError("Weights must sum to 100")

    return sum(a["score"] * a["weight"] / 100 for a in scores)


def calculate_course_average(gradebook: dict, course_id: str) -> float:
    students = gradebook.get(course_id, {})
    if not students:
        return 0.0

    averages = [
        calculate_student_average(gradebook, course_id, sid)
        for sid in students
    ]
    return sum(averages) / len(averages)


def set_grade_policy(course_settings: dict, course_id: str, policy: dict) -> dict:
    course_settings[course_id] = policy  # Store grading policy
    return course_settings


def compute_weighted_score(scores: list[dict], policy: dict) -> float:
    total = 0
    for s in scores:
        category = s["category"]
        total += s["score"] * policy[category] / 100
    return total


def assign_letter_grade(score: float, scale: dict) -> str:
    for letter, threshold in scale.items():
        if score >= threshold:
            return letter
    return "F"

def grade_distribution(gradebook: dict, course_id: str, bins: list[int]) -> dict:
    distribution = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(len(bins) - 1)}

    for student_id in gradebook.get(course_id, {}):
        avg = sum(
            a["score"] * a["weight"] / 100
            for a in gradebook[course_id][student_id].values()
        )
        for i in range(len(bins) - 1):
            if bins[i] <= avg < bins[i + 1]:
                distribution[f"{bins[i]}-{bins[i+1]}"] += 1

    return distribution


def top_performers(gradebook: dict, course_id: str, limit: int = 5) -> list:
    averages = []
    for student_id in gradebook.get(course_id, {}):
        avg = sum(
            a["score"] * a["weight"] / 100
            for a in gradebook[course_id][student_id].values()
        )
        averages.append((student_id, avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    return averages[:limit]


def student_progress_report(gradebook: dict, course_id: str, student_id: str) -> dict:
    assessments = gradebook.get(course_id, {}).get(student_id, {})
    completed = len(assessments)

    average = sum(
        a["score"] * a["weight"] / 100 for a in assessments.values()
    ) if assessments else 0

    return {
        "student_id": student_id,
        "completed_assessments": completed,
        "current_average": average
    }


def export_report(report: dict, filename: str) -> str:
    import json
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename


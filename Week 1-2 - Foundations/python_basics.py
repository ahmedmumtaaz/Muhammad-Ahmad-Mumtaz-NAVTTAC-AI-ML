"""Week 1–2 practice: Python fundamentals. Run with Python 3.10+."""

from pathlib import Path


def grade_label(score: float) -> str:
    """Return a simple grade label for a score from 0 to 100."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "Needs improvement"


def summarize_numbers(numbers: list[float]) -> dict[str, float]:
    """Return count, sum and average for a non-empty list."""
    if not numbers:
        raise ValueError("Provide at least one number.")
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
    }


def main() -> None:
    # Variables, types, operators and formatted strings
    student_name = "Muhammad Ahmad Mumtaz"
    scores = [78, 85, 91, 66, 73]
    print(f"Student: {student_name}")
    print("Score summary:", summarize_numbers(scores))

    # Loops, enumerate, conditionals and list comprehensions
    for index, score in enumerate(scores, start=1):
        print(f"Assessment {index}: {score} ({grade_label(score)})")
    passed_scores = [score for score in scores if score >= 50]
    print("Passed scores:", passed_scores)

    # Dictionary, set and tuple examples
    student = {"name": student_name, "course": "AI/ML", "scores": scores}
    unique_scores = set(scores)
    coordinates = (31.5204, 74.3587)  # example coordinates for Lahore
    print("Student record:", student)
    print("Unique scores:", sorted(unique_scores))
    print("Example coordinates tuple:", coordinates)

    # Exception handling
    try:
        print("Invalid score test:", grade_label(120))
    except ValueError as error:
        print("Handled validation error:", error)

    # File handling: write a small report into the current directory
    report = Path("python_basics_report.txt")
    report.write_text(
        f"Student: {student_name}\nAverage: {sum(scores) / len(scores):.2f}\n",
        encoding="utf-8",
    )
    print(f"Saved report to: {report.resolve()}")


if __name__ == "__main__":
    main()

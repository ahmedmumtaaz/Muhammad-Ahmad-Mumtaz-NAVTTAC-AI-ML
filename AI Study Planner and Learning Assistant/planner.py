"""Explainable priority scoring for study-task recommendations."""
from datetime import date

DIFFICULTY_POINTS = {"easy": 1, "medium": 3, "hard": 5}


def score_task(task, today=None):
    """Return a priority score; larger scores should be studied sooner."""
    today = today or date.today()
    due = date.fromisoformat(task["due_date"])
    days_left = (due - today).days

    if days_left < 0:
        urgency = 12 + min(abs(days_left), 14)
    elif days_left == 0:
        urgency = 12
    elif days_left <= 2:
        urgency = 9
    elif days_left <= 7:
        urgency = 6
    else:
        urgency = 2

    duration_bonus = 1 if int(task["estimated_minutes"]) >= 60 else 0
    return urgency + DIFFICULTY_POINTS.get(task["difficulty"], 1) + duration_bonus


def recommend_task(tasks, today=None):
    """Choose the highest-priority unfinished task, or None."""
    pending = [task for task in tasks if not task.get("completed", 0)]
    if not pending:
        return None
    ranked = sorted(
        pending,
        key=lambda task: (
            score_task(task, today), task["due_date"], task["id"]
        ),
        reverse=True,
    )
    suggestion = dict(ranked[0])
    suggestion["priority_score"] = score_task(suggestion, today)
    suggestion["reason"] = (
        "This task has the strongest combination of deadline urgency and difficulty."
    )
    return suggestion

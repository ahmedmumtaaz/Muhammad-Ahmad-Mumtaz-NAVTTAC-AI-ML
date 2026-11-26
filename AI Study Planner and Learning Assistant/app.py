"""Flask entry point for the AI Study Planner."""
from datetime import date
from flask import Flask, jsonify, render_template, request

from database import (
    add_task, delete_task, get_all_tasks, init_db, set_task_completed,
)
from planner import recommend_task

app = Flask(__name__)
init_db()


def validate_task(payload):
    required = ("title", "subject", "due_date", "estimated_minutes", "difficulty")
    if not isinstance(payload, dict):
        return "Send task details as a JSON object."
    for field in required:
        if not str(payload.get(field, "")).strip():
            return field.replace("_", " ").title() + " is required."
    try:
        date.fromisoformat(payload["due_date"])
        minutes = int(payload["estimated_minutes"])
    except (ValueError, TypeError):
        return "Enter a valid date and a whole-number study duration."
    if minutes < 1 or minutes > 1440:
        return "Study duration must be between 1 and 1440 minutes."
    if payload["difficulty"] not in ("easy", "medium", "hard"):
        return "Difficulty must be easy, medium, or hard."
    if len(payload["title"].strip()) > 100 or len(payload["subject"].strip()) > 60:
        return "Title or subject is too long."
    return None


@app.get("/")
def index():
    tasks = get_all_tasks()
    pending = [task for task in tasks if not task["completed"]]
    completed = [task for task in tasks if task["completed"]]
    return render_template(
        "index.html",
        tasks=tasks,
        pending_count=len(pending),
        completed_count=len(completed),
        total_minutes=sum(task["estimated_minutes"] for task in pending),
        recommendation=recommend_task(tasks),
        today=date.today().isoformat(),
    )


@app.get("/api/tasks")
def api_tasks():
    return jsonify(get_all_tasks())


@app.post("/api/tasks")
def api_add_task():
    payload = request.get_json(silent=True) or {}
    error = validate_task(payload)
    if error:
        return jsonify({"error": error}), 400
    task = add_task(
        payload["title"].strip(), payload["subject"].strip(),
        payload["due_date"], int(payload["estimated_minutes"]),
        payload["difficulty"],
    )
    return jsonify(task), 201


@app.patch("/api/tasks/<int:task_id>")
def api_update_task(task_id):
    payload = request.get_json(silent=True) or {}
    completed = payload.get("completed")
    if not isinstance(completed, bool):
        return jsonify({"error": "The completed field must be true or false."}), 400
    task = set_task_completed(task_id, completed)
    if task is None:
        return jsonify({"error": "Task not found."}), 404
    return jsonify(task)


@app.delete("/api/tasks/<int:task_id>")
def api_delete_task(task_id):
    if not delete_task(task_id):
        return jsonify({"error": "Task not found."}), 404
    return jsonify({"message": "Task deleted."})


@app.get("/api/recommendation")
def api_recommendation():
    suggestion = recommend_task(get_all_tasks())
    return jsonify(suggestion or {"message": "No pending tasks. Great work!"})


if __name__ == "__main__":
    app.run(debug=True)

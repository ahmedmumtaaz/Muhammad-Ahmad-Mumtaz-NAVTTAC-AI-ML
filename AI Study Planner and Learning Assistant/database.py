"""SQLite persistence layer for the Study Planner."""
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("study_planner.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                due_date TEXT NOT NULL,
                estimated_minutes INTEGER NOT NULL CHECK (estimated_minutes > 0),
                difficulty TEXT NOT NULL CHECK (difficulty IN ('easy', 'medium', 'hard')),
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


def get_all_tasks():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM tasks ORDER BY completed ASC, due_date ASC, id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


def add_task(title, subject, due_date, estimated_minutes, difficulty):
    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO tasks
               (title, subject, due_date, estimated_minutes, difficulty)
               VALUES (?, ?, ?, ?, ?)""",
            (title, subject, due_date, estimated_minutes, difficulty),
        )
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?", (cursor.lastrowid,)
        ).fetchone()
    return dict(row)


def set_task_completed(task_id, completed):
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?",
            (1 if completed else 0, task_id),
        )
        if cursor.rowcount == 0:
            return None
        row = connection.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    return dict(row)


def delete_task(task_id):
    with get_connection() as connection:
        cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return cursor.rowcount > 0

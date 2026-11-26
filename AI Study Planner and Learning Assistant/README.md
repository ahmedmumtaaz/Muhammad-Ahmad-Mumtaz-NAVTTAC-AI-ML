# AI Study Planner & Learning Assistant

An original student productivity web app built with Python, Flask, SQLite, HTML, CSS, and JavaScript. It helps learners organize subjects, plan study sessions, track completed work, and receive priority-based study suggestions.

The recommendation engine is a transparent rule-based scoring system, not a hosted LLM. Its logic is explained in planner.py so it can be presented and modified as part of the assignment.

## Features
- Create study tasks with subject, deadline, estimated minutes, and difficulty.
- Mark tasks complete or reopen them; delete tasks.
- Smart suggestions based on deadline urgency and task difficulty.
- Dashboard counters for pending tasks, completed tasks, and remaining study time.
- SQLite storage; no API key or cloud account required.
- JSON API and automated unit tests.

## Structure
    AI Study Planner and Learning Assistant/
    ├── app.py
    ├── database.py
    ├── planner.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    ├── tests/test_planner.py
    ├── templates/index.html
    └── static/
        ├── style.css
        └── app.js

## Run locally
Requires Python 3.10+.

    python -m venv .venv
    # macOS/Linux
    source .venv/bin/activate
    # Windows PowerShell
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python app.py

Open http://127.0.0.1:5000. The database is created automatically.

## Recommendation logic
Each pending task receives points for how soon it is due, whether it is overdue, and how difficult it is. The task with the highest score is recommended. This simple, explainable approach is suitable for demonstrating decision rules and testing.

## API
| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Dashboard |
| GET | /api/tasks | List tasks |
| POST | /api/tasks | Create task |
| PATCH | /api/tasks/<id> | Update completion |
| DELETE | /api/tasks/<id> | Delete task |
| GET | /api/recommendation | Top study suggestion |

Example JSON:
    {
      "title": "Revise decision trees",
      "subject": "Machine Learning",
      "due_date": "2026-12-01",
      "estimated_minutes": 45,
      "difficulty": "medium"
    }

## Run tests
    python -m unittest discover -s tests -v

## Suggested demonstration
1. Add three tasks with different due dates and difficulty levels.
2. Compare the recommended task and explain its score.
3. Complete a task and observe the dashboard update.
4. Refresh the page to demonstrate persistent storage.
5. Run the unit tests.

## Learning outcomes
Flask routing, SQLite persistence, input validation, separation of business logic, a basic recommendation algorithm, frontend/API integration, and unit testing.

## Academic note
Run the project yourself, customize sample tasks and styling, and make sure you can explain each module during your instructor's review.

## Author
Muhammad Ahmad Mumtaz — NAVTTC AI/ML Practice Project

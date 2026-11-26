import unittest
from datetime import date

from planner import recommend_task, score_task


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 11, 26)
        self.tasks = [
            {
                "id": 1, "title": "Read notes", "subject": "AI",
                "due_date": "2026-12-10", "estimated_minutes": 30,
                "difficulty": "easy", "completed": 0,
            },
            {
                "id": 2, "title": "Build classifier", "subject": "ML",
                "due_date": "2026-11-27", "estimated_minutes": 90,
                "difficulty": "hard", "completed": 0,
            },
        ]

    def test_urgent_hard_task_scores_higher(self):
        self.assertGreater(
            score_task(self.tasks[1], self.today),
            score_task(self.tasks[0], self.today),
        )

    def test_recommendation_ignores_completed_tasks(self):
        tasks = [dict(self.tasks[1], completed=1), self.tasks[0]]
        self.assertEqual(recommend_task(tasks, self.today)["id"], 1)

    def test_no_pending_task_returns_none(self):
        tasks = [dict(task, completed=1) for task in self.tasks]
        self.assertIsNone(recommend_task(tasks, self.today))

    def test_overdue_task_gets_urgency_bonus(self):
        overdue = dict(self.tasks[0], due_date="2026-11-20")
        self.assertGreater(score_task(overdue, self.today), 0)


if __name__ == "__main__":
    unittest.main()

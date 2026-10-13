# Muhammad Ahmad Mumtaz — NAVTTC AI/ML

Learning repository for the NAVTTC AI/ML course, organized into the requested three groups:

1. **Week 1–2 — Foundations**: Python, NumPy, Pandas, visualization, mathematics, probability and statistics.
2. **Week 3 — AI/ML and Cloud Platforms**: AI use cases, ML workflow, cloud platform concepts and setup checklist.
3. **Week 4–5 — Data Preparation and Machine Learning**: data cleaning, transformation, feature engineering, regression, classification and evaluation.

## Important note about task numbering
The supplied course-outline PDF lists topics and references ranges such as Task 1–27 and Task 28–55, but does **not** include the complete official question text for each numbered task. The exercises and solutions in this repository are practical implementations aligned with the outline, not a claim that they reproduce the official NAVTTC task sheets verbatim. Add the official task sheets to map each solution to its exact task number.

## Setup

Python 3.10+ is recommended.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
pip install -r requirements.txt
```

Run a script from the repository root, for example:

```bash
python "Week 1-2 - Foundations/python_basics.py"
python "Week 1-2 - Foundations/data_analysis.py"
python "Week 3 - AI-ML and Cloud Platforms/ai_ml_pipeline.py"
python "Week 4-5 - Data Preparation and Machine Learning/data_preparation.py"
python "Week 4-5 - Data Preparation and Machine Learning/machine_learning_models.py"
```

## Folder contents
- Each week group has a README describing the work and learning outcomes.
- Scripts use small, reproducible example datasets so they can run locally without cloud credentials.
- Cloud exercises include setup guidance; provider accounts, credentials and billing are not included.

## Course outline
This repository is based on the course outline provided for the NAVTTC AI/ML course. Official assignment sheets should be used as the source of truth for exact task wording and submission requirements.

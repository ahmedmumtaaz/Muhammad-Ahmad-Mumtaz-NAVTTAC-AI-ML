"""Practice with NumPy, Pandas and Matplotlib using a tiny sample dataset."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    data = {
        "student": ["Ali", "Sara", "Hassan", "Ayesha", "Usman"],
        "python": [78, 92, 67, 88, 74],
        "math": [81, 89, 72, 94, 69],
        "attendance": [90, 98, 82, 96, 85],
    }
    df = pd.DataFrame(data)
    df["average"] = df[["python", "math"]].mean(axis=1)

    print("Dataset preview:\n", df)
    print("\nDescriptive statistics:\n", df[["python", "math", "attendance", "average"]].describe())
    print("\nClass mean:", np.mean(df["average"]))
    print("Class median:", np.median(df["average"]))
    print("\nStudents with average >= 80:\n", df.loc[df["average"] >= 80])

    df.to_csv("student_results.csv", index=False)
    ax = df.plot(x="student", y=["python", "math"], kind="bar", rot=0,
                 title="Student Scores by Subject")
    ax.set_ylabel("Score")
    plt.tight_layout()
    plt.savefig("student_scores.png", dpi=150)
    print("\nSaved student_results.csv and student_scores.png")


if __name__ == "__main__":
    main()

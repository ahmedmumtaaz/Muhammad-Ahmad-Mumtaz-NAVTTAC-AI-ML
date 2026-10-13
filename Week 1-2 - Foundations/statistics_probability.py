"""Descriptive statistics and elementary probability practice."""

from collections import Counter
from math import sqrt
import random


def main() -> None:
    values = [12, 15, 15, 18, 20, 20, 20, 24, 26, 30]
    ordered = sorted(values)
    n = len(ordered)
    median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2 if n % 2 == 0 else ordered[n // 2]
    mean = sum(values) / n
    population_variance = sum((x - mean) ** 2 for x in values) / n
    print("Values:", values)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print("Mode(s):", [v for v, count in Counter(values).items() if count == max(Counter(values).values())])
    print(f"Population variance: {population_variance:.2f}")
    print(f"Population standard deviation: {sqrt(population_variance):.2f}")

    # Theoretical probability for a fair six-sided die
    print("P(rolling a 6) =", 1 / 6)
    print("P(rolling an even number) =", 3 / 6)

    # Simple simulation; the result varies between runs
    random.seed(42)
    rolls = [random.randint(1, 6) for _ in range(10_000)]
    estimated = rolls.count(6) / len(rolls)
    print(f"Simulated P(rolling a 6) over {len(rolls)} rolls = {estimated:.3f}")


if __name__ == "__main__":
    main()

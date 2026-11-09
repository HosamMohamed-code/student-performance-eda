"""Analyze a small CSV dataset of exam scores."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_scores(csv_path):
    """Load the CSV file and validate its score column."""
    data = pd.read_csv(csv_path)

    if "score" not in data.columns:
        raise ValueError("The CSV file must contain a column named 'score'.")

    data["score"] = pd.to_numeric(data["score"], errors="coerce")
    data = data.dropna(subset=["score"])

    if data.empty:
        raise ValueError("No valid numeric scores were found.")

    return data


def calculate_statistics(scores):
    """Calculate and return common descriptive statistics."""
    if len(scores) < 2:
        raise ValueError("At least two scores are needed for sample standard deviation.")

    return {
        "count": int(scores.count()),
        "mean": float(scores.mean()),
        "median": float(scores.median()),
        "minimum": float(scores.min()),
        "maximum": float(scores.max()),
        "sample_std": float(np.std(scores, ddof=1)),
    }


def save_histogram(scores, output_path):
    """Create and save a histogram of the scores."""
    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=5, edgecolor="black")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main():
    # Path(__file__) points to the folder containing this Python file.
    project_folder = Path(__file__).resolve().parent
    csv_path = project_folder / "scores.csv"
    image_path = project_folder / "scores_histogram.png"

    try:
        data = load_scores(csv_path)
        summary = calculate_statistics(data["score"])

        print("===== EXAM SCORE ANALYSIS =====")
        for name, value in summary.items():
            if isinstance(value, float):
                print(f"{name.replace('_', ' ').title()}: {value:.2f}")
            else:
                print(f"{name.replace('_', ' ').title()}: {value}")

        save_histogram(data["score"], image_path)
        print(f"\nHistogram saved to: {image_path}")

    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError) as error:
        print(f"Could not complete the analysis: {error}")


if __name__ == "__main__":
    main()

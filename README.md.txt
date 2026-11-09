# Exploratory Data Analysis & Descriptive Statistics of Exam Scores

A Python-based statistical analysis workflow exploring student performance distribution and summary metrics.

## Overview
This module ingests tabular score records from a CSV file, computes central tendency and dispersion metrics, and visualizes the frequency distribution via a histogram using `pandas`, `numpy`, and `matplotlib`.

## Statistical Metrics Implemented
- **Mean:** $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$
- **Sample Standard Deviation:** $s = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2}$ (`ddof=1`)
- **Median & Range (Min / Max)**

## Requirements & Installation
```bash
pip install -r requirements.txt
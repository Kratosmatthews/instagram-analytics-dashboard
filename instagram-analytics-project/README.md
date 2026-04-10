# Instagram User Analytics Dashboard

A high-scale data analysis project examining engagement patterns and usage behaviors across **1.5 Million+** Instagram users. This project demonstrates a full data pipeline: from raw data processing with **Python**, to deep-dive exploration in **Excel**, and finally interactive storytelling in **Power BI**.

## 📊 Project Overview
The core objective of this project is to identify how demographic factors (Age, Gender) and lifestyle choices correlate with platform engagement. By engineering custom metrics like "Engagement Scores," this analysis provides a granular look at user retention and platform stickiness.

## 📁 Repository Structure
* **`python/`**: Contains `instagram_analysis.py`, the primary script for data cleaning, merging, and feature engineering.
* **`.gitignore`**: Configured to exclude heavy data files and binaries to maintain repository performance.
* **`README.md`**: Project documentation and external resource links.

## 🔗 External Assets (Large Files)
Due to GitHub's file size limitations, the 1.5M+ row datasets and binary workbooks are hosted externally. 

| Asset | Description | Download Link |
| :--- | :--- | :--- |
| **Raw Dataset** | 1.5M row CSV containing user metrics. | [Download Here](https://www.kaggle.com/datasets/rockyt07/social-media-user-analysis) |
| **Power BI Dashboard** | Interactive `.pbix` file with visual insights. | [Download Here](https://drive.google.com/drive/folders/1r-AjetcProhpRTlw5qY1HO5EjoTVzgRP?usp=drive_link) |
| **Excel Analysis** | Spreadsheet containing pivot tables and initial EDA. | [Download Here](https://drive.google.com/drive/folders/1Qvk8JOwRBH91JX4RJbEric9rKomyddcC?usp=drive_link) |

## 🛠️ Data Pipeline & Feature Engineering
The Python analysis script performs the following critical transformations:
* **Engagement Score**: A weighted calculation of `likes`, `comments`, and `posts`.
* **Total Daily Minutes**: A sum of time spent on Feed, Reels, and Explore.
* **Usage Categorization**: Users are binned into *Low*, *Medium*, or *High* based on activity.
* **Demographic Binning**: Age groups are categorized to identify the platform's most active cohorts.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/Kratosmatthews/instagram-analytics-dashboard.git](https://github.com/Kratosmatthews/instagram-analytics-dashboard.git)
cd instagram-analytics-dashboard

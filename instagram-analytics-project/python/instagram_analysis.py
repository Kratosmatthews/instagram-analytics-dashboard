import pandas as pd
import os
import matplotlib.pyplot as plt

# --- 1. SETUP PATHS ---
# Using absolute paths to ensure the script runs correctly across different environments
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_RAW_DIR = os.path.join(BASE_PATH, "..", "data", "raw")
EXPORT_DIR = r"C:\Users\4KTR3Y\Documents\GitHub\.github\instagram-analytics-project\data\cleaned"
EXPORT_FILE = os.path.join(EXPORT_DIR, "instagram_cleaned_data.csv")

# Defining individual file paths
USAGE_PATH = os.path.join(DATA_RAW_DIR, "instagram_usage_lifestyle.csv")
USERS_PATH = os.path.join(DATA_RAW_DIR, "instagram_users_lifestyle.csv")

def main():
    # --- 2. DATA ACQUISITION ---
    print("Loading datasets...")
    try:
        usage = pd.read_csv(USAGE_PATH)
        users = pd.read_csv(USERS_PATH)
    except FileNotFoundError as e:
        print(f"Error: Could not find the data files. {e}")
        return

    # --- 3. DATA MERGING ---
    # To prevent duplicate columns, we only take columns from 'users' that aren't in 'usage'
    cols_to_use = users.columns.difference(usage.columns).tolist()
    cols_to_use.append('user_id')

    print("Merging datasets on user_id...")
    df = pd.merge(usage, users[cols_to_use], on="user_id", how="inner")

    # --- 4. FEATURE ENGINEERING ---
    print("Calculating new engagement and usage metrics...")

    # Calculate Engagement Score
    df['engagement_score'] = (
        df['likes_given_per_day'] + 
        df['comments_written_per_day'] + 
        df['posts_created_per_week']
    )

    # Calculate Total and Average Daily Usage
    df['total_daily_minutes'] = (
        df['time_on_feed_per_day'] + 
        df['time_on_reels_per_day'] + 
        df['time_on_explore_per_day']
    )
    df['average_feature_usage'] = df['total_daily_minutes'] / 3

    # Categorize Usage Levels
    def get_usage_label(mins):
        if mins < 30:
            return 'Low'
        elif mins < 120:
            return 'Medium'
        else:
            return 'High'

    df['usage_category'] = df['total_daily_minutes'].apply(get_usage_label)

    # Create Age Groups for Analysis
    age_bins = [0, 18, 25, 35, 50, 100]
    age_labels = ['Under 18', '18-25', '26-35', '36-50', '50+']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

    # --- 5. DATA AGGREGATION & REPORTING ---
    print("\n--- DATASET SUMMARY ---")
    print(f"Total Record Count: {len(df):,}")

    # Grouping by Gender
    gender_analysis = df.groupby('gender')['total_daily_minutes'].mean().round(2)
    print("\nMean Daily Usage (Minutes) by Gender:")
    print(gender_analysis)

    # Identifying Top Performers
    top_engaged = df.nlargest(10, 'engagement_score')[['user_id', 'engagement_score', 'usage_category']]
    print("\nTop 10 Users by Engagement Score:")
    print(top_engaged.to_string(index=False))

    # --- 6. DATA EXPORT ---
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
        
    print(f"\nExporting cleaned data to: {EXPORT_FILE}")
    df.to_csv(EXPORT_FILE, index=False)
    print("Export successful.")

    # --- 7. VISUALIZATION ---
    print("Generating usage visualization...")
    plt.figure(figsize=(10, 6))
    
    # Setting a professional color palette
    colors = ['#5dade2', '#ec7063', '#58d68d']
    gender_analysis.plot(kind="bar", color=colors)

    plt.title("Average Instagram Usage by Gender", fontsize=14)
    plt.xlabel("Gender", fontsize=12)
    plt.ylabel("Minutes Per Day", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
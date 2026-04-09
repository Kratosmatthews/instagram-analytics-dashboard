import pandas as pd
import os
import matplotlib.pyplot as plt

base_path = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(base_path, "..", "data", "raw")
export_path = r"C:\Users\4KTR3Y\Documents\GitHub\.github\instagram-analytics-project\data\cleaned\instagram_cleaned_data.csv"

usage_file = os.path.join(data_folder, "instagram_usage_lifestyle.csv")
users_file = os.path.join(data_folder, "instagram_users_lifestyle.csv")

usage = pd.read_csv(usage_file)
users = pd.read_csv(users_file)

cols_to_use = users.columns.difference(usage.columns).tolist() + ['user_id']
df = pd.merge(usage, users[cols_to_use], on="user_id", how="inner")

df['engagement_score'] = (df['likes_given_per_day'] + 
                          df['comments_written_per_day'] + 
                          df['posts_created_per_week'])

df['total_daily_minutes'] = (df['time_on_feed_per_day'] + 
                             df['time_on_reels_per_day'] + 
                             df['time_on_explore_per_day'])

df['average_usage'] = df['total_daily_minutes'] / 3

def create_usage_category(mins):
    if mins < 30: return 'Low'
    if mins < 120: return 'Medium'
    return 'High'

df['usage_category'] = df['total_daily_minutes'].apply(create_usage_category)

df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 50, 100], 
                         labels=['Under 18', '18-25', '26-35', '36-50', '50+'])

gender_usage = df.groupby('gender')['total_daily_minutes'].mean()
age_usage = df.groupby('age_group')['total_daily_minutes'].mean()
top_users = df.nlargest(10, 'engagement_score')[['user_id', 'engagement_score', 'usage_category']]

print("--- Dataset Statistics ---")
print(f"Total Rows: {len(df):,}")
print("\nUsage by Gender:\n", gender_usage)
print("\nTop 10 Users by Engagement:\n", top_users)

os.makedirs(os.path.dirname(export_path), exist_ok=True)
df.to_csv(export_path, index=False)
print(f"\n💾 Data exported to: {export_path}")

plt.figure(figsize=(10, 6))
gender_usage.plot(kind="bar", color=['#FF9999', '#66B3FF', '#99FF99'])
plt.title("Average Usage by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Minutes Per Day")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
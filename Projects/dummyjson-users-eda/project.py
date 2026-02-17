"""
DummyJSON Users - EDA Project 

Requirements:
- Fetch ALL users from DummyJSON API using pagination (limit/skip)
- Flatten nested JSON into a DataFrame
- Basic exploration + cleaning
- Answer analysis questions
- Create at least 5 plots (and save them locally)

Run:
    python project.py

Outputs:
    outputs/users.csv
    outputs/plots/*.png
"""

import os
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 0) Settings
# -----------------------------
BASE_URL = "https://dummyjson.com/users"
LIMIT = 100
TIMEOUT = 20

OUTPUT_DIR = "outputs"
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

# -----------------------------
# 1) Load data from API (ALL pages)
# -----------------------------
skip = 0
rows = []

print("Downloading users from API...")

while True:
    r = requests.get(BASE_URL, params={"limit": LIMIT, "skip": skip}, timeout=TIMEOUT)
    r.raise_for_status()

    payload = r.json()                 # full response as dict
    users_page = payload.get("users", [])
    total = payload.get("total", 0)

    rows.extend(users_page)

    skip += LIMIT
    if skip >= total:
        break

# Flatten nested JSON (address.country, hair.color, company.name, etc.)
df_raw = pd.json_normalize(rows)

# Save raw dataset
csv_path = os.path.join(OUTPUT_DIR, "users.csv")
df_raw.to_csv(csv_path, index=False)
print(f"Saved dataset to {csv_path}")

# -----------------------------
# 2) Basic Data Exploration
# -----------------------------
print("\n" + "=" * 60)
print("BASIC DATA EXPLORATION")
print("=" * 60)

print("\n1) Shape (rows, cols):", df_raw.shape)

print("\n2) Column names:")
print(df_raw.columns.tolist())

print("\n3) Data types:")
print(df_raw.dtypes)

print("\n4) Missing values per column (top 25):")
missing = df_raw.isnull().sum().sort_values(ascending=False)
print(missing.head(25))

print("\n5) Duplicate rows:", df_raw.duplicated().sum())

print("\n6) Summary statistics (numeric columns):")
# Works on old pandas too (avoid numeric_only arg)
print(df_raw.select_dtypes(include="number").describe())

print("\n7) Value counts for important categorical columns:")
cat_cols = ["gender", "bloodGroup", "eyeColor", "role", "address.country"]
for col in cat_cols:
    print(f"\n--- {col} ---")
    if col in df_raw.columns:
        print(df_raw[col].value_counts(dropna=False))
    else:
        print("Column not found.")

# -----------------------------
# 3) Data Cleaning / Preparation
# -----------------------------
df = df_raw.copy()

# Make sure numeric types are correct + fill missing with median
for col in ["age", "height", "weight"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

# -----------------------------
# 4) Analysis + Visualizations
# -----------------------------
print("\n" + "=" * 60)
print("ANALYSIS")
print("=" * 60)

sns.set_theme()

# 1) Average age
avg_age = df["age"].mean()
print("\n1) Average age of users:", avg_age)

plt.figure(figsize=(7, 4))
sns.histplot(df["age"], kde=True)
plt.axvline(avg_age, color="red", linestyle="--", label="Mean Age")
plt.title("Age Distribution (with Mean)")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "01_age_distribution.png"), dpi=150)
plt.close()

# 2) Average age by gender
avg_age_gender = df.groupby("gender")["age"].mean()
print("\n2) Average age by gender:")
print(avg_age_gender)

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="gender", y="age", estimator="mean", errorbar=None)
plt.title("Average Age by Gender")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "02_avg_age_by_gender.png"), dpi=150)
plt.close()

# 3) Number of users per gender
users_per_gender = df["gender"].value_counts(dropna=False)
print("\n3) Number of users per gender:")
print(users_per_gender)

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="gender")
plt.title("Users per Gender")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "03_users_per_gender.png"), dpi=150)
plt.close()

# 4) Top 10 cities
top_cities = df["address.city"].value_counts().head(10)
print("\n4) Top 10 cities with the most users:")
print(top_cities)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_cities.values, y=top_cities.index, errorbar=None)
plt.title("Top 10 Cities by User Count")
plt.xlabel("User Count")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "04_top_10_cities.png"), dpi=150)
plt.close()

# 5) Average height and weight overall
avg_height = df["height"].mean()
avg_weight = df["weight"].mean()
print("\n5) Average height and weight overall:")
print("Avg height:", avg_height)
print("Avg weight:", avg_weight)

plt.figure(figsize=(6, 4))
sns.barplot(x=["Height", "Weight"], y=[avg_height, avg_weight], errorbar=None)
plt.title("Average Height vs Average Weight")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "05_avg_height_vs_weight.png"), dpi=150)
plt.close()

# 6) Relationship between age and height/weight (correlation + regression)
corr_age_height = df["age"].corr(df["height"])
corr_age_weight = df["age"].corr(df["weight"])
print("\n6) Relationship (correlation):")
print("Corr(age,height):", corr_age_height)
print("Corr(age,weight):", corr_age_weight)

plt.figure(figsize=(6, 4))
sns.regplot(data=df, x="age", y="height", scatter_kws={"alpha": 0.5})
plt.title("Age vs Height")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "06_age_vs_height.png"), dpi=150)
plt.close()

plt.figure(figsize=(6, 4))
sns.regplot(data=df, x="age", y="weight", scatter_kws={"alpha": 0.5})
plt.title("Age vs Weight")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "07_age_vs_weight.png"), dpi=150)
plt.close()

print("\nDone ")
print(f"CSV saved: {csv_path}")
print(f"Plots saved in: {PLOTS_DIR}")

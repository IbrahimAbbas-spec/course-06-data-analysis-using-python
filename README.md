# Course 06 — Data Analysis Using Python (ITI Data Engineering Track)

This repository contains my **labs** and **projects** for Course 06: *Data Analysis Using Python*.

## Repository Structure
- `labs/` → practice notebooks/scripts from the course
- `projects/` → end-to-end projects (EDA, cleaning, visualization, etc.)

## Projects
### 1) DummyJSON Users — EDA
- Folder: `projects/dummyjson-users-eda/`
- What it does:
  - Fetches all users from DummyJSON API using pagination
  - Flattens nested JSON into a pandas DataFrame
  - Performs basic exploration and cleaning
  - Produces plots and exports CSV

## How to Run
```bash
pip install -r requirements.txt
python projects/dummyjson-users-eda/project.py

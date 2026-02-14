import numpy as np
import pandas as pd
df =pd.read_csv('students.csv', parse_dates=["Score Date"])
print(df)
##################################################################################
##################################################################################
# •Fill missing Grade values with the average Grade.

df['Grade'].fillna(df['Grade'].mean(), inplace= True)
print(df)
##################################################################################
# •Fill missing Score Date values with the most common date (mode).

df['Score Date']=df['Score Date'].fillna(df['Score Date'].mode()[0])
print(df['Score Date'])
##################################################################################
# •Add a new column Final_Grade = Grade + 5 (bonus points).

df['Final_Grade']=df['Grade']+5
print(df)
##################################################################################
# •Create a column Grade_Category using pd.cut with bins:
# •0–69 → "Fail"
# •70–79 → "Average"
# •80–89 → "Good"
# •90–100 → "Excellent"

df['Grade_Category']=pd.cut(df['Grade'],
                            bins=[0, 70, 80, 90, 100],
                            labels=['Fail', 'Average', 'Good', 'Excellent'],
                            include_lowest= True)
print(df)
##################################################################################
# •Remove the column Student ID.

df=df.drop(columns='Student ID')
print(df)
##################################################################################
# •Keep only students who Passed.

df=df[df['Passed']== True]
print(df)
##################################################################################
# •Sort the DataFrame by Grade descending.

print(df.sort_values('Grade', ascending=False))
##################################################################################
# •Sort by City ascending, then inside each city sort by Grade descending.

print(df.sort_values(['City', 'Grade'], ascending=[True, False]))
##################################################################################
# •Add a column Rank that ranks students by Grade (1 = highest, handle ties with 'min').

df['Rank_min']=df['Student ID'].rank(ascending=False, method='min')
print(df)
##################################################################################
# •Show the top 4 students with the highest grades (use nlargest).

print(df.nlargest(4, 'Grade'))
##################################################################################
# •Show the 3 youngest students (use nsmallest on Age).

print(df.nsmallest(3, 'Age'))
##################################################################################
# •Find the student(s) with the highest Grade and show their Name and Grade.

print(df.nlargest(1, 'Grade')[['Name', 'Age']])
##################################################################################
# •After filling missing grades, recalculate the average Grade per Subject.

df['Grade']=df['Grade'].fillna(df['Grade'].mean())
print(df)
print(df.groupby('Subject')['Grade'].mean())
##################################################################################
# Create a new column City_Avg that shows the average grade of each student's city (using transform).
df['City_Avg']=df.groupby('City')['Grade'].transform('mean')
print(df['City_Avg'])
##################################################################################
# •Show the subject with the highest average grade.

print(df.groupby('Subject')['Grade'].mean().idxmax())
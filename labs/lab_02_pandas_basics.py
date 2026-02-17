import numpy as np
import pandas as pd
##################################################################################
# •Load the file students.csv and make sure Score Date is parsed as datetime.
df =pd.read_csv('students.csv', parse_dates=["Score Date"])
print(df)
##################################################################################
# •Print the shape, columns list, and data types of the DataFrame.

print(df.shape)
print(df.columns)
print(df.dtypes)
##################################################################################
# •Show the first 7 rows and the last 3 rows

print(df.head(7))
print(df.tail(3))
##################################################################################
# •Show how many missing values in each column.

print(df.isna().sum())
##################################################################################
# •What is the average, minimum, and maximum Grade?

print(df["Grade"].agg(['mean','min','max']))
##################################################################################
# •How many unique cities are there? List them.

print(df['City'].nunique())
print(df['City'].unique())
##################################################################################
# •Use value_counts() to show how many students per Subject.

print(df['Subject'].value_counts())
print(df.groupby('Subject')['Name'].count())
##################################################################################
# •Select only the columns: Name, Grade, Subject, City.

print(df[['Name', 'Grade', 'Subject', 'City']])
##################################################################################
# •Show all students who Passed and have Grade ≥ 85.

print(df[(df['Passed']== True) & (df['Grade']>=85)])
##################################################################################
# •Show students whose Name contains the letter "a" or "A" (case insensitive).

print(df[df['Name'].str.contains('a', case=False)])
##################################################################################
# •Show students in Cairo or Alexandria with Grade < 80.

print(df[(df['City'].isin(['Cairo', 'Alexandria'])) & (df['Grade'] < 80)])
##################################################################################
# •Show students with Grade between 80 and 90 (inclusive).

print(df[df['Grade'].between(80, 90)])
##################################################################################
# •Using .loc, change Khaled's grade from 55 to 68.

df.loc[df['Name']=='Khaled', 'Grade']=68
print(df)
##################################################################################
# Add a new column Is_Excellent that is True if Grade ≥ 90, False otherwise (vectorized).

df['Is_Excellent']=np.where(df['Grade']>= 90,'Yes','No')
df['Is_Excellent']=df['Grade'].apply(lambda x: 'Yes' if x >=90 else 'No')

# ## 1. Project Overview
# 
# This project explores student performance data using Python.
# 
# ## 2. Objectives
# 
# - Inspect.
# - Identify missing values.
# - Calculate summary statistics.
# - Visualize score patterns.
# 
# ## 3. Tools
# 
# - Jupyter Notebook
# - Python
# - Pandas
# - Matplotlib
# 

student_scores = [78, 85, 92, 67, 88, 76, 95, 81]

total_students = len(student_scores)
average_score = sum(student_scores) / total_students

print("Total Students: ", total_students)
print("Average Score: ", average_score)
print("Highest Score: ", max(student_scores))
print("Lowest Score: ", min(student_scores))


# ## 4. Data Quality Checks
# 
# Before analysing data, we should check for missing values, duplicate records, and unexpected values.

student_scores = [78, 85, 92, 67, 88, 76, 95, 81]

print("Number of Records: ", len(student_scores))  
print("Missing scores: ", student_scores.count(None))  #Counts missing values represented by None 
print("Duplicate scores: ", len(student_scores) - len(set(student_scores))) #set command keeps unique values
print("Minimum scores: ", min(student_scores)) 
print("Maximum scores: ", max(student_scores))

# ## 5. Loading and Exploring the Dataset
# 
# We use pandas to load structured data, inspect its columns, and identify potential data-quality issues.

!mamba install pandas

import pandas as pd

df = pd.read_csv("Student.csv")

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()


print("Average Math score is: ", df["math_score"].mean())

# ## 6. Exploratory Data Analysis (EDA)
# 
# 

df.sort_values(   #sorts the rows by math score.
    by="math_score",
    ascending=False  #sorts from highest to lowest.
).head(5)

df[["study_hours", "math_score"]]

df["study_hours"].corr(df["math_score"])  #Correlation ranges from -1 to +1.- Near +1: a strong positive linear relationship.- Near 0: little or no linear relationship.- Near -1: a strong negative linear relationship.

df["attendance_percent"].corr(df["math_score"])

df

# ### Initial Findings
# 
# - The highest recorded math score was 96, belonging to student 108.
# - Student 108 also had 6 study hours and 98% attendance.
# - Study hours and math scores had a Pearson correlation of approximately 0.971.
# - Attendance and math scores had a Pearson correlation of approximately 0.970.
# - Both variables showed very strong positive linear associations with math scores in this dataset.
# - These correlations do not establish causation, and the small sample limits generalization.

# ## 7. Data Cleaning

df.isnull().sum()

df[df["math_score"].isnull()]

missing_percent = df.isnull().mean() * 100 # Gives the percentage of missing values in each column.
missing_percent

df_analysis = df.dropna(subset=["math_score"]).copy()

print("Original shape:", df.shape)
print("Analysis shape:", df_analysis.shape)
print("Missing math scores:", df_analysis["math_score"].isnull().sum())

df.loc[df["math_score"].isnull(), "student_id"]

# ## 8. Visualizing Student Performance
# 
# Visualizations make the findings easier to understand and help the project look more professional.

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.scatter(
    df_analysis["study_hours"],
    df_analysis["math_score"]
)

plt.title("Study Hours vs Math Scores")
plt.xlabel("Study Hours")
plt.ylabel("Math Score")
plt.grid(True, alpha=0.3)

plt.show()

plt.figure(figsize=(8, 5))

plt.scatter(
    df_analysis["attendance_percent"],
    df_analysis["math_score"]
)

plt.title("Attendance vs Math Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Math Score")
plt.grid(True, alpha=0.3)

plt.show()

average_scores = df_analysis[
    ["math_score", "english_score"]
    ].mean()

average_scores.plot(
    kind="bar", 
    figsize=(7, 5)
)

plt.title("Average Math vs English Scores")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.show()


#Bar CHart: Useful for comparing Categories

summary = df_analysis[
    ["study_hours", "attendance_percent",
     "math_score", "english_score"]
].describe()

summary

print("Average math score:", round(df_analysis["math_score"].mean(), 2))
print("Average English score:", round(df_analysis["english_score"].mean(), 2))
print("Average study hours:", round(df_analysis["study_hours"].mean(), 2))
print("Average attendance:", round(df_analysis["attendance_percent"].mean(), 2), "%")

# ## Key Findings
# 
# - The dataset contains 10 student records and 5 columns.
# - One math score was missing, leaving 9 complete records for analyses involving math scores.
# - The average math score among the analyzed students was 80.44.
# - The average English score among the analyzed students was 81.89.
# - Average study time was approximately 3.56 hours, and average attendance was 82.78%.
# - Study hours and attendance each showed a very strong positive correlation with math scores in this dataset.
# 
# ## Limitations
# 
# - The dataset is small, containing only 10 student records.
# - The missing math score was excluded from analyses involving math scores; this may affect the results.
# - Correlation does not establish causation.
# - The results describe this practice dataset and cannot be generalized to all students.


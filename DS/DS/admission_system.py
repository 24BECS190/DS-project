import pandas as pd
import numpy as np

# -------------------------
# Data Acquisition
# -------------------------
df = pd.read_csv("admission_data.csv")

print("===== UNIVERSITY ADMISSION ANALYTICS SYSTEM =====")

# -------------------------
# Dataset Inspection
# -------------------------
print("\nFirst 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

# -------------------------
# Data Profiling
# -------------------------
print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDepartment Count")
print(df["Department"].value_counts())

# -------------------------
# Data Validation
# -------------------------
print("\nChecking Invalid Marks")

invalid_marks = df[(df["Marks"] < 0) | (df["Marks"] > 100)]

if invalid_marks.empty:
    print("No Invalid Marks Found")
else:
    print(invalid_marks)

# -------------------------
# NumPy Operations
# -------------------------
marks = np.array(df["Marks"])

print("\nNumPy Operations")

print("Average Marks :", np.mean(marks))
print("Highest Marks :", np.max(marks))
print("Lowest Marks :", np.min(marks))
print("Standard Deviation :", np.std(marks))

# -------------------------
# Python Function
# -------------------------
def admission_status(mark):
    if mark >= 85:
        return "Admitted"
    elif mark >= 70:
        return "Waiting List"
    else:
        return "Rejected"

df["Admission_Status"] = df["Marks"].apply(admission_status)

print("\nAdmission Result")
print(df[["Name","Marks","Admission_Status"]])

# -------------------------
# Top Students
# -------------------------
print("\nTop 3 Students")

top = df.sort_values(by="Marks", ascending=False)

print(top.head(3))

# -------------------------
# Average Marks by Department
# -------------------------
print("\nAverage Marks Department Wise")

print(df.groupby("Department")["Marks"].mean())

print("\nProgram Completed Successfully")
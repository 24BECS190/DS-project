import pandas as pd
import numpy as np
import glob

print("========== SMART CITY TRAFFIC MANAGEMENT SYSTEM ==========")

# -----------------------------
# Multi-file Processing
# -----------------------------
files = glob.glob("traffic_day*.csv")

print("\nCSV Files Found:")
print(files)

# -----------------------------
# Data Integration
# -----------------------------
dataframes = []

for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

traffic = pd.concat(dataframes, ignore_index=True)

print("\nCombined Dataset")
print(traffic)

# -----------------------------
# Dataset Inspection
# -----------------------------
print("\nShape of Dataset")
print(traffic.shape)

print("\nColumn Names")
print(traffic.columns)

print("\nDataset Information")
traffic.info()

# -----------------------------
# Missing Value Detection
# -----------------------------
print("\nMissing Values")
print(traffic.isnull().sum())

# Replace missing vehicle count with average
traffic["Vehicle_Count"] = traffic["Vehicle_Count"].fillna(
    traffic["Vehicle_Count"].mean()
)

print("\nDataset After Filling Missing Values")
print(traffic)

# -----------------------------
# NumPy Operations
# -----------------------------
vehicles = np.array(traffic["Vehicle_Count"])

print("\nNumPy Statistics")

print("Average Vehicles :", np.mean(vehicles))
print("Maximum Vehicles :", np.max(vehicles))
print("Minimum Vehicles :", np.min(vehicles))
print("Standard Deviation :", np.std(vehicles))

# -----------------------------
# Python Function
# -----------------------------
def traffic_status(count):
    if count >= 250:
        return "Heavy Traffic"
    elif count >= 150:
        return "Moderate Traffic"
    else:
        return "Light Traffic"

traffic["Traffic_Status"] = traffic["Vehicle_Count"].apply(traffic_status)

print("\nTraffic Status")
print(traffic[["Junction","Vehicle_Count","Traffic_Status"]])

# -----------------------------
# Junction-wise Average
# -----------------------------
print("\nAverage Vehicle Count by Junction")

print(traffic.groupby("Junction")["Vehicle_Count"].mean())

print("\nProgram Completed Successfully")
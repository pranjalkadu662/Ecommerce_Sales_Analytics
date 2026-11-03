import pandas as pd

df = pd.read_csv("Dataset/Sample - Superstore.csv", encoding="latin-1")

# 1. Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")

# 2. Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# 3. Check missing values and duplicates
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# 4. Add useful columns for analysis
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month_name()

# 5. Quick summary
print(df.describe())
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

# 6. Save cleaned file
df.to_csv("Dataset/Superstore_Cleaned.csv", index=False)
print("Cleaned file saved!")
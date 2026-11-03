import pandas as pd

df = pd.read_csv("Dataset/Superstore_Cleaned.csv")

print("Total Orders:", df["Order_ID"].nunique())
print("Total Customers:", df["Customer_ID"].nunique())

print("\nSales by Category:")
print(df.groupby("Category")[["Sales", "Profit"]].sum().round(2))

print("\nSales by Region:")
print(df.groupby("Region")[["Sales", "Profit"]].sum().round(2))

print("\nTop 10 Products by Sales:")
print(df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(10).round(2))

print("\nSales by Year:")
print(df.groupby("Year")["Sales"].sum().round(2))
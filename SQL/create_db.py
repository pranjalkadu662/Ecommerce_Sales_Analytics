import sqlite3
import pandas as pd

df = pd.read_csv("Dataset/Superstore_Cleaned.csv")

conn = sqlite3.connect("SQL/superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)

# Test query
result = pd.read_sql("SELECT COUNT(*) AS total_rows FROM orders", conn)
print(result)

conn.close()
print("Database created!")
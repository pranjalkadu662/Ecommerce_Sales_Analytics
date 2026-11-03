import sqlite3
import pandas as pd

conn = sqlite3.connect("SQL/superstore.db")

queries = {
"1. Total Sales, Profit, Orders, Customers": """
    SELECT ROUND(SUM(Sales),2) AS total_sales,
           ROUND(SUM(Profit),2) AS total_profit,
           COUNT(DISTINCT Order_ID) AS total_orders,
           COUNT(DISTINCT Customer_ID) AS total_customers
    FROM orders""",

"2. Sales and Profit by Category": """
    SELECT Category, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY Category ORDER BY sales DESC""",

"3. Sales by Region": """
    SELECT Region, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY Region ORDER BY sales DESC""",

"4. Top 10 Products by Sales": """
    SELECT Product_Name, ROUND(SUM(Sales),2) AS sales
    FROM orders GROUP BY Product_Name ORDER BY sales DESC LIMIT 10""",

"5. Top 10 Customers by Sales": """
    SELECT Customer_Name, ROUND(SUM(Sales),2) AS sales
    FROM orders GROUP BY Customer_Name ORDER BY sales DESC LIMIT 10""",

"6. Sales by Year": """
    SELECT Year, ROUND(SUM(Sales),2) AS sales
    FROM orders GROUP BY Year ORDER BY Year""",

"7. Sales by Segment": """
    SELECT Segment, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY Segment""",

"8. Loss-making Sub-Categories": """
    SELECT Sub_Category, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY Sub_Category HAVING profit < 0 ORDER BY profit""",

"9. Average Discount by Category": """
    SELECT Category, ROUND(AVG(Discount),3) AS avg_discount
    FROM orders GROUP BY Category""",

"10. Top 5 States by Profit": """
    SELECT State, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY State ORDER BY profit DESC LIMIT 5""",

"11. Monthly Sales Trend": """
    SELECT Year, Month, ROUND(SUM(Sales),2) AS sales
    FROM orders GROUP BY Year, Month ORDER BY Year, MIN(Order_Date)""",

"12. Profit Margin % by Category": """
    SELECT Category, ROUND(SUM(Profit)*100.0/SUM(Sales),2) AS margin_pct
    FROM orders GROUP BY Category ORDER BY margin_pct DESC""",

"13. Profit Margin % by Sub-Category": """
    SELECT Sub_Category, ROUND(SUM(Profit)*100.0/SUM(Sales),2) AS margin_pct
    FROM orders GROUP BY Sub_Category ORDER BY margin_pct""",

"14. Sales by Ship Mode": """
    SELECT Ship_Mode, COUNT(*) AS orders, ROUND(SUM(Sales),2) AS sales
    FROM orders GROUP BY Ship_Mode ORDER BY sales DESC""",

"15. Repeat Customers (3+ orders)": """
    SELECT COUNT(*) AS repeat_customers FROM (
        SELECT Customer_ID FROM orders
        GROUP BY Customer_ID HAVING COUNT(DISTINCT Order_ID) >= 3)""",

"16. Average Order Value": """
    SELECT ROUND(SUM(Sales)/COUNT(DISTINCT Order_ID),2) AS avg_order_value
    FROM orders""",

"17. Discount Effect on Profit": """
    SELECT CASE WHEN Discount = 0 THEN 'No discount'
                WHEN Discount <= 0.2 THEN 'Up to 20%'
                ELSE 'Over 20%' END AS discount_band,
           ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY discount_band""",

"18. Bottom 10 States by Profit": """
    SELECT State, ROUND(SUM(Profit),2) AS profit
    FROM orders GROUP BY State ORDER BY profit LIMIT 10""",

"19. Year-over-Year Sales Growth %": """
    SELECT Year, ROUND(SUM(Sales),2) AS sales,
           ROUND((SUM(Sales) - LAG(SUM(Sales)) OVER (ORDER BY Year))*100.0
                 / LAG(SUM(Sales)) OVER (ORDER BY Year),2) AS growth_pct
    FROM orders GROUP BY Year""",

"20. Top Product per Category": """
    SELECT Category, Product_Name, sales FROM (
        SELECT Category, Product_Name, ROUND(SUM(Sales),2) AS sales,
               RANK() OVER (PARTITION BY Category ORDER BY SUM(Sales) DESC) AS rnk
        FROM orders GROUP BY Category, Product_Name)
    WHERE rnk = 1""",
}

for title, q in queries.items():
    print("\n" + title)
    print(pd.read_sql(q, conn).to_string(index=False))

conn.close()
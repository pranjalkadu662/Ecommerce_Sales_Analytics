# Ecommerce Sales Analytics

An end-to-end sales analytics project built with **Excel, Python, SQL,
and Power BI** using the Sample Superstore dataset. The project explores
sales, profit, customers, products, categories, regions, order trends,
and discount impact.

## Project Overview

The goal of this project is to turn Superstore sales data into useful
business insights through data cleaning, exploratory data analysis, SQL
queries, and a Power BI dashboard.

## Tools & Technologies

-   **Microsoft Excel** --- spreadsheet-based data work
-   **Python** --- data cleaning and exploratory data analysis
-   **SQL** --- database creation and business queries
-   **Power BI** --- dashboard design and data visualization

## Repository Structure

``` text
Ecommerce_Sales_Analytics/
├── Excel/
|── Dataset/
│   ├── Sample - Superstore
│   └── Superstore_Cleaned
├── Python/
│   ├── cleaning.py
│   └── eda.py
├── PowerBI/
│   ├── Ecommerce_Sales_Analytics
│   └── Ecommerce_Sales_Dashboard
├── SQL/
│   ├── create_db.py
│   ├── run_queries.py
│   ├── superstore
│   ├── 03_sql_output.png
│   └── 04_sql_output_part2.png
├── Screenshots/
│   ├── 00_eda_output
│   ├── 03_sql_output
│   ├── 04_sql_output_part2
│   └── Ecommerce_Sales_Dashboard
└── README.md
```

## Project Workflow

1.  Prepared the Sample Superstore dataset and a cleaned version.
2.  Used Python for data cleaning.
3.  Performed exploratory data analysis on sales, profit, categories,
    regions, products, customers, and yearly trends.
4.  Created a database and ran SQL queries to answer business questions.
5.  Built a Power BI dashboard to present key metrics and sales
    breakdowns.
6.  Saved screenshots of the dashboard and analysis outputs as project
    evidence.

## Power BI Dashboard

The **E-Commerce Sales & Customer Analytics** dashboard presents these
headline metrics:

  KPI                 Result
  -------------- -----------
  Total Sales        \$2.30M
  Total Profit     \$286.40K
  Customers              793
  Orders               5,009

The dashboard includes: - Sales by category - Sales trends by year and
month - Top products by sales - Sales by region - Filters for customer
segment, category, and region

## Key Business Findings

The following findings are based on the SQL analysis outputs shown in
this project.

### 1. Overall Performance

-   Total sales: **\$2,297,200.86**
-   Total profit: **\$286,397.02**
-   Total orders: **5,009**
-   Total customers: **793**
-   Average order value: **\$458.61**

### 2. Category Performance

  Category                   Sales         Profit
  ----------------- -------------- --------------
  Technology          \$836,154.03   \$145,454.95
  Furniture           \$741,999.80    \$18,451.27
  Office Supplies     \$719,047.03   \$122,490.80

Technology generated the highest sales and profit. Furniture generated
substantial sales but comparatively lower profit.

### 3. Regional Performance

  Region             Sales         Profit
  --------- -------------- --------------
  West        \$725,457.82   \$108,418.45
  East        \$678,781.24    \$91,522.78
  Central     \$501,239.89    \$39,706.36
  South       \$391,721.91    \$46,749.43

The West region recorded the highest sales and profit. The South region
had the lowest sales.

### 4. Year-over-Year Sales Growth

  Year            Sales     Growth
  ------ -------------- ----------
  2014     \$484,247.50   Baseline
  2015     \$470,532.51     -2.83%
  2016     \$609,205.60     29.47%
  2017     \$733,215.26     20.36%

Sales declined slightly in 2015, then increased in 2016 and 2017.

### 5. Discount Effect on Profit

  Discount band            Profit
  --------------- ---------------
  No discount        \$320,987.60
  Up to 20%          \$100,785.47
  Over 20%          -\$135,376.06

Orders with discounts above 20% had a negative total profit in this
analysis, suggesting that high discount levels should be reviewed
carefully.

### 6. Product Highlights

-   **Canon imageCLASS 2200 Advanced Copier** was the highest-selling
    product shown in the SQL output, with sales of **\$61,599.82**.
-   The top Furniture product shown was **HON 5400 Series Task Chairs
    for Big and Tall**, with sales of **\$21,870.58**.
-   The top Office Supplies product shown was **Fellowes PB500 Electric
    Punch Plastic Comb Binding Machine**, with sales of **\$27,453.38**.

## Screenshots

Project evidence is stored in the `Screenshots` and `SQL` folders. These
images document the Power BI dashboard, exploratory analysis, and SQL
query outputs.

## Dataset

This project uses the **Sample Superstore** dataset and a cleaned
version prepared for analysis. Please follow the original dataset
provider's terms and license when sharing or redistributing the dataset.

## How to Explore

1.  Clone or download this repository.
2.  Open the Excel files with Microsoft Excel.
3.  Run the Python scripts in a Python environment with the required
    packages installed.
4.  Open the SQL database and scripts with a compatible database tool.
5.  Open the Power BI report with Power BI Desktop.

File paths may need to be adjusted when the project is opened on another
computer.

## Author

**Pranjal Kadu**

GitHub: [@pranjalkadu662](https://github.com/pranjalkadu662)

------------------------------------------------------------------------

Thanks for visiting this project!

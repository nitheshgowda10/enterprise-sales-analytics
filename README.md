# 📊 Enterprise Sales Analytics & Reporting Solution  

## 📌 Project Overview  
This project is an **end-to-end Data Analytics solution** built using:  
- **Python** (ETL – Extract, Transform, Load)  
- **MySQL** (Database for structured storage)  
- **Power BI** (Interactive dashboards for insights)  

It demonstrates how raw enterprise sales data can be processed, cleaned, stored, and transformed into **business intelligence dashboards** to support decision-making.  

---

## 🚀 Features  
✔️ Automated **data ingestion** from CSV into MySQL using Python  
✔️ Data **cleaning and transformation** (remove duplicates, handle null values)  
✔️ **Relational database** schema in MySQL for analytics  
✔️ **Power BI dashboards** with KPIs, sales insights, customer trends, and product analysis  
✔️ Exportable reports in **PDF format** for sharing  

---

## 🛠️ Tech Stack  
- **Programming**: Python (Pandas, SQLAlchemy, dotenv)  
- **Database**: MySQL  
- **Visualization**: Power BI  
- **Version Control**: Git + GitHub  

---

## 📂 Project Structure  
enterprise-sales-analytics/
│
├── data/
│   └── Global_superstore2.csv
│
├── src/
│   └── load_data.py
│
├── dashboard/
│   └── enterprise_sales.pbix     ← Your Power BI file
│   └── dashboards.pdf            ← Exported PDF of dashboards
│
├── docs/
│   └── Project_Report.pdf        ← The detailed report
│
├── .env.example                  ← Example env file 
├── requirements.txt              ← Python libraries list
├── README.md                     ← Summary of project

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/nitheshgowda10/enterprise-sales-analytics.git
cd enterprise-sales-analytics


2️⃣ Setup Virtual Environment
python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate   # (Mac/Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=analytics
DB_PORT=3306

5️⃣ Load Data into MySQL

Run the Python script:

python src/load_data.py


This script will:

Read the CSV dataset

Remove duplicates & null values

Load the cleaned dataset into MySQL (analytics.superstore table)

6️⃣ Connect Power BI

Open dashboard.pbix in Power BI Desktop

Connect to MySQL database (analytics schema, superstore table)

Refresh data and explore dashboards

📊 Power BI Dashboards

The dashboard is divided into 4 interactive pages:

🔹 Page 1: Sales Overview

KPIs: Total Sales, Total Profit, Profit Margin %

Sales Trend (line chart by month/year)

Sales by Region (Map)

Top 10 Products by Sales (Bar Chart)

Purpose: Gives management a high-level overview of business performance.

🔹 Page 2: Market & Category Insights

KPIs: Total Sales, Profit, Profit Margin %

Sales by Market (Treemap)

Top Category by Profit (Bar Chart)

Lowest Margin Sub-Category (Table/Bar)

Purpose: Helps identify which markets and product categories are most profitable vs loss-making.

🔹 Page 3: Customer Insights

KPIs:

Total Customers = DISTINCTCOUNT(Customer ID)

Top Customer by Sales = MAX Sales per Customer

Average Order Value (AOV) = Sales ÷ Number of Orders

Customer Sales Distribution (Histogram/Bar Chart)

Scatter Plot: Sales vs Profit by Customer

Purpose: Understand customer behavior, identify high-value customers, and detect loss-making ones.

🔹 Page 4: Product Insights

Top 10 Products by Sales (Bar Chart)

Top 10 Products by Profit (Bar Chart)

Sub-Category Profitability (Treemap/Bar Chart)

Product Returns or Negative Profit Cases

Purpose: Helps in product strategy – know which products drive growth and which cause losses.

📑 Final Deliverables

✔️ Cleaned dataset in MySQL database
✔️ Python ETL script (load_data.py)
✔️ SQL queries for data analysis
✔️ Power BI Dashboard (dashboard.pbix)
✔️ Final Report (report.pdf)
✔️ GitHub Repository with code & documentation

🚀 Key Learnings

Designed a complete ETL pipeline using Python

Worked with MySQL relational databases

Built SQL queries for analytical insights

Designed professional dashboards in Power BI

Demonstrated an end-to-end Data Analytics project

📌 Author

👤 Name : Nithesh Gowda HG
📧 email : gowdanithesh28@gmail.com

🔗 GitHub Profile : https://github.com/nitheshgowda10

🔗 LinkedIn Profile : https://www.linkedin.com/in/nithesh-gowda-h-g-ba1b08299

# 📊 Vendor Performance Analysis

## Executive Summary

This project delivers a **data-driven evaluation of vendor performance** to improve inventory management, pricing strategies, and vendor relationships in a **retail/wholesale business context**. By integrating purchase, sales, and vendor cost data, the analysis uncovers hidden profitability patterns, operational risks, and actionable optimization opportunities.

The solution is built using **Python, SQL, and SQLite**, and culminates in a **BI-style analytical dashboard** and recommendation framework designed to support strategic decision-making.

---

## 📊 BI Dashboard Preview

> Sample dashboard visuals for vendor performance analytics

![Vendor Performance Dashboard](https://images.tableau.com/solutions/vendoranalytics/VendorAnalyticsDashboard.png)

🔗 **Reference dashboards:**
- https://public.tableau.com/en-us/s/resources
- https://www.microsoft.com/en-us/power-platform/products/power-bi
- https://lookerstudio.google.com/

---

## 🎯 Business Objectives

- Identify **underperforming brands** suitable for promotion or pricing changes  
- Determine **top vendors** based on sales and purchase contribution  
- Measure the **impact of bulk purchasing** on unit costs  
- Evaluate **inventory turnover** to reduce holding costs  
- Compare **profitability** between high- and low-performing vendors  

---

## 🗂️ Dataset Overview

The project uses structured transactional and inventory data stored in CSV format:

- **purchases.csv** – Transaction-level purchase records  
- **purchase_prices.csv** – Product pricing and unit cost details  
- **vendor_invoice.csv** – Vendor billing and freight costs  
- **sales.csv** – Sales transaction data  
- **begin_inventory.csv / end_inventory.csv** – Inventory snapshots *(excluded)*  

---

## 🧠 Methodology

### 1️⃣ Data Ingestion
- Loaded CSV files into **SQLite (`inventory.db`)**
- Automated ingestion using `load_raw_data.py`
- Tables created dynamically based on filenames

### 2️⃣ Exploratory Data Analysis (EDA)
- Schema and relationship exploration using SQL
- Removed irrelevant inventory snapshot tables

### 3️⃣ Data Aggregation
- Created **vendor_sales_summary**
- Joined purchase, sales, pricing, and vendor invoice tables
- Computed KPIs:
  - Total sales & purchase quantity
  - Gross profit & profit margin
  - Inventory turnover
  - Sales-to-purchase ratio

### 4️⃣ Data Cleaning
- Converted volume fields to numeric
- Handled missing values
- Standardized categorical columns
- Added calculated metrics

### 5️⃣ Analysis
- Brand performance analysis
- Vendor contribution assessment
- Bulk purchasing cost impact
- Inventory turnover evaluation
- Vendor profitability comparison

### 6️⃣ Statistical Validation
- Performed **t-test** to validate margin differences

---

## 📈 Key Findings

### 🔹 Underperforming Brands
- **198 brands** with low sales but high margins
- Example: *Santa Rita Organic Svgn Bl* – **66.47% margin**

### 🔹 Vendor Dependency
- Top 10 vendors = **65.69% of total purchases**
- Diageo North America alone = **16.30%**

### 🔹 Bulk Purchasing
- Unit cost reduction of **~72%**
- Small orders: **$39.06/unit**
- Large orders: **$10.78/unit**

### 🔹 Inventory Turnover
- **$2.71M** unsold inventory identified
- Diageo: **$722.21K** slow-moving stock

### 🔹 Profitability
- Low-performing vendors: **41.55% margin**
- Top vendors:

# 🛒 E-Commerce Product Analysis using Web Scraping, Python & Power BI

## 📌 Project Overview

This project demonstrates an **end-to-end e-commerce data analysis workflow** by scraping real product data from **Flipkart**, performing data cleaning and analysis using **Python**, and building an interactive **Power BI dashboard** to generate actionable business insights.

The objective is to understand **pricing strategies, product quality, value-for-money offerings, and product positioning** in the online retail space.

---

## 🎯 Objectives

* Collect real-time e-commerce product data using **web scraping**
* Analyze relationships between **price, rating, and product value**
* Identify **best value-for-money products**, **overpriced items**, and **hidden gems**
* Present insights through an interactive Power BI dashboard

---

## 🌐 Data Collection (Web Scraping)

* Website: **Flipkart**
* Category Scraped: **Earphones**
* Technique: `requests` + `BeautifulSoup`
* Pages Scraped: Multiple pages for broader coverage

### Scraped Fields:

* Product Name
* Price
* Rating

The scraped data is stored in a CSV file for further analysis.

---

## 🛠 Tools & Technologies Used

* **Python** (Requests, BeautifulSoup, Pandas)
* **Power BI** (Data visualization & dashboarding)
* **GitHub** (Version control & documentation)

---

## 🧹 Data Cleaning & Processing

* Removed currency symbols and commas from price
* Converted price to numeric format
* Converted ratings to float
* Handled missing and inconsistent values

---

## 📊 Key KPIs

* **Average Price**
* **Average Rating**
* **Total Number of Products**

---

## 📈 Dashboard Visualizations (Power BI)

### 🔹 Scatter Plot

* **Price vs Rating**
* Helps identify overpriced products and hidden gems

### 🔹 Bar Chart

* **Top 10 Rated Products**
* Highlights high-quality products based on user ratings

### 🔹 Slicers

* **Price Range**
* **Rating Filter**
* **Top 10 Best Value-for-Money Products**

---

## 💡 Advanced Analysis Performed

### ✅ Price Band Classification

Products were segmented into:

* **Low:** ₹0 – ₹1,000
* **Mid:** ₹1,001 – ₹2,000
* **High:** ₹2,000+

This helps analyze customer preferences across different price segments.

---

### ✅ Value-for-Money Analysis

A custom metric was used to identify products offering **high ratings at lower prices**, helping uncover:

* Best value-for-money products
* Budget-friendly high-quality items

---

### ✅ Overpriced Products

* Identified products with **high prices but relatively low ratings**
* Useful for pricing strategy and quality improvement decisions

---

### ✅ Hidden Gems

* Products with **low price and high rating**
* These represent strong promotional opportunities for sellers

---

## 📌 Business Insights

* Mid-range products tend to offer better value-for-money compared to premium items
* Some high-priced products are overrated compared to lower-priced alternatives
* Budget-friendly products with high ratings are often overlooked but highly competitive

---

## 🚀 Conclusion

This project showcases how **real-world e-commerce data** can be collected, analyzed, and visualized to support **business decision-making**. It combines **web scraping**, **data analysis**, and **dashboard storytelling**, making it a strong portfolio project for **Data Analyst** roles.


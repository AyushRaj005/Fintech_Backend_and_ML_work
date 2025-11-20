# Stock Analysis & Prediction System

*A Full-Stack ML-Powered Platform for Company Insights, Fundamental Analysis & Stock Price Forecasting*

## Overview

This project is an **end-to-end stock analysis system** that integrates:

* A **relational database** storing company profiles, financial analysis, and pros/cons
* An **ML Engine** for stock price forecasting using **LSTM**
* A **Stock Analysis Pipeline** for extracting growth metrics, CAGR values, ROE, and more
* (Optional) API endpoints or dashboards built over this backend

The system is designed to combine **fundamental analysis + machine learning predictions** to create a unified financial intelligence tool.


# 🏗️ System Architecture

## 🔹 1. Database Schema

Your database is organised into three main tables:

### **companies**

Stores basic details and metadata about listed companies.

| Field                             | Type          | Description         |
| --------------------------------- | ------------- | ------------------- |
| id                                | varchar       | Primary key         |
| company_logo                      | varchar       | Logo URL            |
| company_name                      | varchar       | Full name           |
| chart_link                        | varchar       | Chart link for UI   |
| about_company                     | text          | Company description |
| website, nse_profile, bse_profile | varchar       | External links      |
| face_value                        | int           |                     |
| book_value                        | int           |                     |
| roce_percentage                   | decimal(12,2) |                     |
| roe_percentage                    | decimal(12,2) |                     |

---

### **analysis**

Stores company-specific analysis metrics.

| Field                    | Type                            |
| ------------------------ | ------------------------------- |
| id                       | varchar(10)                     |
| company_id               | varchar(10) (FK → companies.id) |
| compounded_sales_growth  | varchar(50)                     |
| compounded_profit_growth | varchar(50)                     |
| stock_price_cagr         | varchar(50)                     |
| roe                      | varchar(50)                     |

---

### **prosandcons**

Stores pros/cons generated for each company.

| Field      | Type                             |
| ---------- | -------------------------------- |
| id         | int                              |
| company_id | varchar(255) (FK → companies.id) |
| pros       | varchar                          |
| cons       | varchar                          |

---

## 🔹 2. ML Modules

Your system includes two major ML components:

### * A. Stock Price Prediction – LSTM Model**
Features include:

* Data loading using yfinance
* Sliding window preparation
* LSTM with 50–100 units
* Train/test split
* MinMax scaling
* Multi-day ahead forecasting
* Model visualisations

### ** B. ML Financial Analyser**

(Referenced from your shared ChatGPT link)

Performs:

* CAGR calculations
* ROE extraction
* Sales & profit growth
* Analyst-style summarisation
* Pros/Cons auto-generation
* Integration with database tables


# Features

### **Company Data Module**

* Stores detailed metadata
* Fetches external links (NSE/BSE, website)
* Supports company-profile APIs

### **Financial Analysis Engine**

* Growth rate computation
* CAGR & ROE extraction
* Sector-wise comparisons
* Auto-generated Pros/Cons using ML or rules

### **ML LSTM Stock Predictor**

* Time-series modelling
* Long-term & short-term forecasting
* Graphical predictions
* Easy retraining with daily live data

### **Backend (Optional)**

* REST APIs for company details
* APIs for ML-predicted prices
* APIs for financial analysis outputs

---

# How the System Works (Flow)

1. **User selects a company**
2. System fetches its **company profile** from `companies` table
3. Financial analyser loads:

   * ROE
   * CAGR
   * Sales & profit growth
   * Pros/cons
4. LSTM module loads the stock’s historical data
5. Predicts next 30 or 60 days of prices
6. All outputs displayed in UI/API

---

# Installation

### Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/stock-analysis-system.git
cd stock-analysis-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set up MySQL database

```sql
CREATE DATABASE stock_system;
USE stock_system;
SOURCE database/schema.sql;
```

### Run backend (optional)

```bash
python api/app.py
```

---

# Sample Outputs

### **LSTM Prediction Graph**

* Stock closing price
* Predicted vs actual
* Future trend line

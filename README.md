# Predictive-Financial-Analytics
A data analytics and predictive modeling project performing Multiple Linear Regression to analyze the impact of R&amp;D, Administration, and Marketing expenditures on startup profitability.
# Startup Profitability & Expenditure Analysis

## 📌 Project Overview
This project explores the financial performance of 50 startups to evaluate how resource allocation across key operational departments—**Research & Development (R&D)**, **Administration**, and **Marketing**—affects total company revenue and profitability. 

Using **Multiple Linear Regression**, this model predicts startup net profit based on spending habits across different geographic regions.

---

## 📊 Dataset Summary
* **Records:** 50 Startups
* **Location Scope:** New York, California, Florida
* **Features:**
  * `RD_Spend`: Total expenditure in Research & Development
  * `Administration`: Total administrative and managerial expenditure
  * `Marketing_Spend`: Total advertising and marketing expenditure
  * `State`: Operational base of the startup
* **Target Variable:** `Profit`: Net income generated

---

## 📈 Model Performance & Statistical Results

The dataset was analyzed using Multiple Linear Regression:

| Metric | Value |
| :--- | :--- |
| **Multiple R** | 0.9751 |
| **R-Squared ($R^2$)** | 0.9507 |
| **Adjusted $R^2$** | 0.9475 |
| **Standard Error** | 9,232.33 |
| **Observations** | 50 |

### Regression Formula
$$\text{Profit} = 50122.19 + (0.8057 \times \text{RD\_Spend}) - (0.0268 \times \text{Administration}) + (0.0272 \times \text{Marketing\_Spend})$$

---

## 💡 Key Findings & Strategic Insights

1. **R&D Spend is the Main Driver:** R&D expenditure has a high positive impact on profit ($p < 0.001$). For every \$1,000 invested in R&D, net profit increases by approximately **\$805.70**.
2. **Administration Has Minimal Effect:** Administrative spending shows a slight negative correlation ($-0.0268$) but is statistically insignificant ($p = 0.601$).
3. **Marketing Yields Moderate Growth:** Marketing shows a positive relationship ($+0.0272$), but its impact is substantially smaller than direct R&D investments.

---

## 📁 Repository Structure

```text
├── Sales_Details_Raw_Data.csv    # Raw dataset containing 50 startups spending data
├── Sales_Details_Answer.xlsx     # Excel file with ANOVA tables, regression metrics, and predictions
└── README.md                     # Project documentation

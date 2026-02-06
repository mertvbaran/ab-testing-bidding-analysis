# A/B Testing: Comparison of Bidding Strategies

## Project Overview
This project evaluates the performance of the newly introduced **Average Bidding** strategy against the legacy **Maximum Bidding** method for the e-commerce platform *bombabomba.com*. The primary objective is to determine whether the new strategy leads to a statistically significant increase in the **Purchase** metric, which is defined as the ultimate success criterion for the client.

---

## Dataset Characteristics
The analysis is based on 1 month of A/B test data containing the following metrics:
* **Control Group:** Maximum Bidding.
* **Test Group:** Average Bidding.
* **Key Metrics:** Impressions, Clicks, Purchase (Target), and Earning.

---

## Statistical Methodology

### 1. Assumption Testing
Before conducting the hypothesis test, the data was checked for the following statistical assumptions:
* **Normality:** Shapiro-Wilk test was applied to both groups to ensure data follows a normal distribution.
* **Variance Homogeneity:** Levene’s test was utilized to check the equality of variances between the groups.

### 2. Hypothesis Testing
As both normality and variance homogeneity assumptions were met (p > 0.05), an **Independent Two-Sample T-Test** was performed to compare the means of the "Purchase" variable.

---

## Findings and Business Recommendations

### Visual Analysis
![Purchase Comparison](outputs/purchase_comparison.png)

### Test Results
* **P-Value:** 0.3493
* **Decision:** Fail to reject the Null Hypothesis (H0).

### Executive Summary
The statistical analysis indicates **no significant difference** between the two bidding strategies regarding total purchases (p > 0.05). From a data-driven perspective, transitioning to "Average Bidding" does not yield a measurable conversion advantage based on the current 1-month sample size.

---

## Technical Setup
1. **Requirements:** `pandas`, `scipy`, `matplotlib`, `seaborn`, `openpyxl`.
2. **Execution:** Run the following command in your terminal to generate the report and visualizations:
   ```bash
   python scripts/main_analysis.py
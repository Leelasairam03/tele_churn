-- 1. Overall churn rate
SELECT COUNT(*) AS total_customers,
       SUM(Churn_flag) AS churned,
       ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 2) AS churn_rate_pct
FROM customers;

-- 2. Churn by contract type
SELECT Contract, COUNT(*) AS customers,
       ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- 3. Churn by tenure group
SELECT CASE WHEN tenure <= 12 THEN '0-12 months'
            WHEN tenure <= 24 THEN '13-24 months'
            WHEN tenure <= 48 THEN '25-48 months'
            ELSE '49+ months' END AS tenure_group,
       COUNT(*) AS customers,
       ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY tenure_group
ORDER BY churn_rate_pct DESC;

-- 4. Churn by payment method
SELECT PaymentMethod, COUNT(*) AS customers,
       ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;

-- 5. Average monthly charges: churned vs retained
SELECT Churn, ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM customers
GROUP BY Churn;

-- 6. Riskiest segments (contract + internet service)
SELECT Contract, InternetService, COUNT(*) AS customers,
       ROUND(100.0 * SUM(Churn_flag) / COUNT(*), 2) AS churn_rate_pct
FROM customers
GROUP BY Contract, InternetService
HAVING COUNT(*) > 100
ORDER BY churn_rate_pct DESC;
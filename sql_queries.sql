 PhonePe Transaction Insights
-- SQL Queries for Data Analysis


-- 1. View transaction data
SELECT *
FROM aggregated_transaction
LIMIT 10;


-- 2. Total transaction amount
SELECT SUM(transaction_amount) AS total_transaction_amount
FROM aggregated_transaction;


-- 3. Total transaction count
SELECT SUM(transaction_count) AS total_transaction_count
FROM aggregated_transaction;


-- 4. State-wise transaction amount
SELECT
    state,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC;


-- 5. Top 10 states by transaction amount
SELECT
    state,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;


-- 6. Year-wise transaction trend
SELECT
    year,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;


-- 7. Transaction type analysis
SELECT
    transaction_type,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_count
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- 8. State and year-wise transactions
SELECT
    state,
    year,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state, year
ORDER BY state, year;


-- 9. Quarter-wise transaction analysis
SELECT
    year,
    quarter,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_count
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;


-- 10. Average transaction value
SELECT
    SUM(transaction_amount) / NULLIF(SUM(transaction_count), 0)
        AS average_transaction_value
FROM aggregated_transaction;

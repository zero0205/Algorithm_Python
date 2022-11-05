SELECT YEAR(CREATED_AT) AS YEAR, MONTH(CREATED_AT) AS MONTH, COUNT(*) AS CANCEL_COUNT, SUM(AMOUNT) AS AMOUNT
FROM CARD_USAGES
GROUP BY (YEAR(CREATED_AT), MONTH(CREATED_AT));
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, A.PRICE*B.TOTAL AS TOTAL_SALES
    FROM FOOD_PRODUCT A
    INNER JOIN (SELECT PRODUCT_ID, SUM(AMOUNT) AS TOTAL
                     FROM FOOD_ORDER
                     WHERE TO_CHAR(PRODUCE_DATE, 'YYYY-MM') = '2022-05'
                     GROUP BY PRODUCT_ID) B
    ON A.PRODUCT_ID = B.PRODUCT_ID
    ORDER BY 3 DESC, 1
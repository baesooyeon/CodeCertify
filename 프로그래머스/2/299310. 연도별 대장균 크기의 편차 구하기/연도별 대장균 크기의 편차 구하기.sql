-- 코드를 작성해주세요
-- 코드를 작성해주세요
SELECT YEAR(A.DIFFERENTIATION_DATE) AS YEAR,
    C.MAX_SIZE - A.SIZE_OF_COLONY AS YEAR_DEV,
    A.ID
FROM ECOLI_DATA A 
    LEFT JOIN (
        SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) MAX_SIZE
        FROM ECOLI_DATA
        GROUP BY YEAR(DIFFERENTIATION_DATE)
    ) C
ON YEAR(A.DIFFERENTIATION_DATE) = C.YEAR
ORDER BY YEAR, YEAR_DEV
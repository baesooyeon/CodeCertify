-- 코드를 작성해주세요
SELECT COUNT(B.FISH_NAME) FISH_COUNT, B.FISH_NAME
FROM FISH_INFO AS A
LEFT JOIN FISH_NAME_INFO AS B
ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY B.FISH_NAME
ORDER BY FISH_COUNT DESC
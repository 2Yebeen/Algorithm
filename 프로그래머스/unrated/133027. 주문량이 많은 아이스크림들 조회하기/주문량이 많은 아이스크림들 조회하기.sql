/*
7월 아이스크림 총 주문량
+
상반기의 아이스크림 총 주문량
값이 큰 순서대로 
상위 3개의 맛을 조회
*/

SELECT F.FLAVOR
  FROM FIRST_HALF AS F 
       LEFT JOIN JULY AS J
       ON F.FLAVOR = J.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
         LIMIT 3

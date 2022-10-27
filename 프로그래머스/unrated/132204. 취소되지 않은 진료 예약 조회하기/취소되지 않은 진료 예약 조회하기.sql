# PATIENT, DOCTOR 그리고 APPOINMENT 테이블에서 
# 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력
# 진료예약일시를 기준으로 오름차순 정렬해주세요.

SELECT 
    A.APNT_NO
    , P.PT_NAME
    , P.PT_NO
    , A.MCDP_CD
    , D.DR_NAME
    , A.APNT_YMD
FROM 
    APPOINTMENT AS A
    INNER JOIN DOCTOR AS D ON A.MDDR_ID = D.DR_ID
    INNER JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
WHERE 
    DATE_FORMAT(A.APNT_YMD ,'%Y-%m-%d') ='2022-04-13'
    AND A.MCDP_CD = 'CS' 
    AND (A.APNT_CNCL_YN = 'N' OR A.APNT_CNCL_YMD IS NULL)
ORDER BY A.APNT_YMD

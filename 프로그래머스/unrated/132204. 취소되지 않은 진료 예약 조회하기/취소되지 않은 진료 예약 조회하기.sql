-- 코드를 입력하세요
# PATIENT 
# PT_NO 환자번호
# , PT_NAME 환자이름
# , GEND_CD 성별코드
# , AGE 나이
# , TLNO 전화번호

# DOCTOR 
# DR_NAME 의사이름
# , DR_ID 의사ID
# , LCNS_NO 면허번호
# , HIRE_YMD 고용일자
# , MCDP_CD 진료과코드
# , TLNO 전화번호

# APPOINTMENT 
# APNT_YMD 진료예약일시
# , APNT_NO 진료예약번호
# , PT_NO 환자번호
# , MCDP_CD 진료과코드
# , MDDR_ID 의사ID
# , APNT_CNCL_YN 예약취소여부
# , APNT_CNCL_YMD 예약취소날짜

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
    INNER JOIN DOCTOR AS D ON A.MCDP_CD = D.MCDP_CD AND A.MDDR_ID = D.DR_ID
    INNER JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
WHERE 
    YEAR(A.APNT_YMD) = 2022 AND MONTH(A.APNT_YMD) = 4 AND DAY(A.APNT_YMD) = 13
    AND A.MCDP_CD = 'CS' 
    AND (A.APNT_CNCL_YN = 'N' OR A.APNT_CNCL_YMD IS NULL)

ORDER BY A.APNT_YMD

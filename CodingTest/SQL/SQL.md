# SQL

[TOC]



## Programmers

### SELECT

##### 모든 레코드 조회하기

```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```



##### 역순 정렬하기

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;
```



##### 아픈 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION='Sick';
```



##### 어린 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION NOT IN('Aged') ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID;
```



##### 동물의 아이디와 이름

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```



##### 여러 기준으로 정렬하기

```sql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;
```



##### 상위 n개 레코드

```sql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1;
```





### SUM, MAX, MIN

- 중복된 개수를 제외하고 싶다면
  - COUNT(DISTINCT 컬럼)
    - COUNT 괄호안에 DISTINCT 입력하기



##### 최댓값 구하기

```sql
SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;

SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS;
```



##### 최솟값 구하기

```sql
SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS;
```



##### 동물 수 구하기

```sql
SELECT COUNT(*) AS COUNT FROM ANIMAL_INS;
```



##### 중복 제거하기

```sql
SELECT COUNT(DISTINCT NAME) AS count FROM ANIMAL_INS WHERE NAME IS NOT NULL;
```



### GROUP BY

- **SELECT** ``컬럼A``, ``컬럼B`` **FROM** ``테이블`` **GROUP BY** ``컬럼A``
  - 그룹화하는 컬럼은 반드시 SELECT로 조회해야함.



##### 고양이와 개는 몇 마리 있을까

```sql
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;
```



##### 동명 동물 수 찾기

```sql
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME;
```



##### 입양 시각 구하기(1)

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT FROM ANIMAL_OUTS GROUP BY HOUR HAVING HOUR BETWEEN 9 AND 19 ORDER BY HOUR(DATETIME);
```



##### 입양 시각 구하기(2)

```sql
SET @HOUR = -1;
SELECT ( @HOUR := @HOUR + 1) AS HOUR, 
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
```





### IS NULL

- **IFNULL** (컬럼, A)
  - 컬럼이 Null 이면 A를 표시, Null이 아니면 컬럼의 값을 출력
- **ISNULL** (컬럼, A)
  - 컬럼이 Null 이면 A로 표시


##### 이름이 있는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL;

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID;
```



##### NULL 처리하기

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS;

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```





### JOIN

- 두 테이블의 데이터를 일정한 조건에 의해 연결하여 마치 하나의 테이블처럼 만드는 것

  - **INNER JOIN**과 **OUTER JOIN**이 많이 쓰임

    - **INNER JOIN**
      - 기준 테이블과 조인 테이블에 모두 데이터가 존재해야함
      - **SELECT** ``컬럼`` **FROM** ``테이블A`` **INNER JOIN** ``테이블B`` **ON** ``조인될 조건`` (**WHERE** ``검색조건``)
    - **LEFT OUTER JOIN**
      - 왼쪽 테이블 기준으로 조건에 맞는 오른쪽 테이블의 데이터를 가져옴
      - 없으면 NULL 표시
    - **FULL OUTER JOIN**
      - 두 테이블을 합쳐서 조회
      - JOIN이 되면 해당 값을 표시하고, 안되면 NULL 표시

  - **(LEFT) JOIN** vs **(LEFT) OUTER JOIN**
    - 단일 **JOIN**은 빈 값은 안가져오고, **OUTER JOIN**은 빈 값까지 가져온다.

  - 테이블 3개 조인

    - 학생 테이블(StudentTable)과 동아리 테이블(StdClubTable), 동아리 방번호 테이블(ClubTable) 조인하기

    ```sql
    SELECT S.Name, Addr, C.Name, RoomNo
    FROM StudentTable S
    	INNER JOIN StdClubTable SC
    	ON S.NAME = SC.StdName
    		INNER JOIN ClubTable C
    		ON SC.ClubName = C.Name
    ```




##### 없어진 기록 찾기

- **SELECT** ``OUTS.ANIMAL_ID``, ``OUTS.NAME``
  - 왼쪽 데이터를 기준으로 ANIMAL_ID와 NAME 데이터 조회
- **FROM** ``ANIMAL_OUTS OUTS`` **LEFT OUTER JOIN** ``ANIMAL_INS INS``
  - 입양을 간 기록이 존재하므로, 존재하는 기록을 바탕으로 존재하지 않는 데이터를 조회하기 위함
- **ON** ``OUTS.ANIMAL_ID`` = ``INS.ANIMAL_ID``
  - ANIMAL_ID를 기준으로 데이터 유무 차이를 판단함
- **WHERE** `INS.ANIMAL_ID` **is NULL**
  - JOIN 이후에 왼쪽 테이블 기준으로 오른쪽 테이블의 데이터가 없으면 NULL이 표시되므로 is NULL 조건 사용
- **ORDER BY** `OUTS.ANIMAL_ID`
  - ID 순으로 조회

```sql
# JOIN
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS 
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID

# 서브쿼리
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS) # ANIMAL_INS의 ANIMAL_ID가 ANIMAL_OUTS에 없는 경우
```



##### 있었는데요 없었습니다

- **SELECT** ``OUTS.ANIMAL_ID``, ``OUTS.NAME``
  - ANIMAL_ID, NAME 데이터 조회 (OUTS에서 가져오든 INS에서 가져오든 상관없음)
- **FROM** ``ANIMAL_OUTS OUTS`` **LEFT OUTER JOIN** ``ANIMAL_INS INS``
  - 보호 시작일과 입양일을 연결해야하므로 (왼쪽에 INS가 들어가도 상관없음)
- **ON** ``OUTS.ANIMAL_ID`` = ``INS.ANIMAL_ID``
  - ANIMAL_ID가 외래키이므로 기준이 됨
- **WHERE** ``OUTS.DATETIME`` < ``INS.DATETIME``
  - 보호 시작일보다 입양일이 더 빠른 동물을 찾아야함
- **ORDER BY** ``INS.DATETIME``
  - 보호 시작일이 빠른 순으로 조회

```sql
# OUTER JOIN
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME

# INNER JOIN
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME

# JOIN 미사용
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID and INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME
```



##### 오랜 기간 보호한 동물(1)

- **SELECT** ``INS.NAME``, ``INS.DATETIME``
  - NAME, DATETIME 조회
- **FROM** ``ANIMAL_INS INS`` **LEFT OUTER JOIN** ``ANIMAL_OUTS OUTS``
  - 보호소 기준으로 입양보낸 동물을 확인하여 입양 못간 동물 체크
- **ON** ``INS.ANIMAL_ID`` = ``OUTS.ANIMAL_ID``
  - ANIMAL_ID가 외래키이므로 기준이 됨
- **WHERE** ``OUTS.ANIMAL_ID`` **is NULL**
  - 보호소 기준으로 입양을 가지 못한 동물이면 NULL이므로 NULL 조건
- **ORDER BY** ``INS.DATETIME`` **LIMIT** 3;
  - 보호 시작일 순으로 3마리 조회

```sql
# JOIN
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME LIMIT 3;

# 서브쿼리
SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY DATETIME LIMIT 3;
```



##### 보호소에서 중성화한 동물

- **SELECT** ``INS.ANIMAL_ID``, ``INS_ANIMAL_TYPE``, ``INS.NAME``
  - ANIMAL_ID, ANIMAL_TYPE, NAME 조회
- **FROM** ``ANIMAL_INS INS`` **LEFT OUTER JOIN** ``ANIMAL_OUTS OUTS``
  - 보호소 기준으로 입양보낸 동물을 확인
- **ON** ``INS.ANIMAL_ID`` = ``OUTS.ANIMAL_ID``
  - ANIMAL_ID가 외래키이므로 기준이 됨
- **WHERE** ``INS.SEX_UPON_INTAKE`` != ``OUTS.SEX_UPON_OUTCOME``
  - SEX_UPON_INTAKE는 보호소에 들어올 당시 중성화 여부, SEX_UPON_OUTCOME은 보호소를 나갈 당시 중성화 여부를 알려준다.
  - 보호소에 들어올 당시 중성화 여부 -> 보호소를 나갈 당시 중성화 여부 (첫번째)
  - 보호소에 들어올 당시 중성화 되지 않은 경우 -> 보호소를 나갈 당시 중성화된 여부(두번째)
  - 두번째를 찾아야 하므로 ``!=`` 혹은 ``NOT LIKE``를 사용하여 조건을 걸어준다.

```sql
# OUTER JOIN
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME

# INNER JOIN
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE ('Intact%') AND (OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY INS.ANIMAL_ID

# 서브쿼리
# INS의 ANIMAL_ID가 OUTS의 중성화된 동물들의 ID와 일치하고, INS의 중성화 여부가 되지 않은 경우 = INS일때 중성화X -> OUTS일때 중성화O
SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_INS
WHERE ANIMAL_ID IN (SELECT ANIMAL_ID
                   FROM ANIMAL_OUTS
                   WHERE SEX_UPON_OUTCOME IN ('Spayed Female', 'Neutered Male')
                   )
AND SEX_UPON_INTAKE IN ('Intact Male', 'Intact Female')
ORDER BY ANIMAL_ID
```





### String, Date

- 조건문

  - **CASE WHEN** ``조건문`` **THEN** ``참일때 값`` **ELSE** ``거짓일때 값`` **END** ``컬럼명``

    - 예시) 테이블(TB)에서 성별(GENDER)이 01이면 남, 그게 아니면 여자

    ```SQL
    CASE WHEN GENDER = '01' THEN '남' ELSE '여' END AS 성별
    ```

    - 예시) SALARY(연봉)에 따른  성과 등급을 출력 (다중 CASE)

    ```SQL
    EMP_NO NAME SALARY
    000001	김	5000
    000002	이	5500
    000003	박	6000
    000004	최	4500
    000005	정	4000
    
    # EMP_NO, NAME, SALARY, 성과를 나타내시오.
    
    SELECT EMP_NO, NAME, SALARY
    	CASE
    	WHEN SALARY >= 5500 THEN 'A'
    	WHEN SALARY BETWEEN 5000 AND 5500 THEN 'B'
    	WHEN SALARY BETWEEN 4500 AND 5000 THEN 'C'
    	ELSE 'D'
    	END AS 성과
    FROM TB
    ```

  - **IF** ``조건문``, ``참일때 값``, ``거짓일때 값``

    - 예시) 테이블에서 회원이 NULL인 경우는 X 표시, 맞으면 회원을 출력

    ```sql
    IF (ISNULL(MEMBER), 'X', MEMBER)
    ```

  - **IF** ``조건문`` **THEN** ``결과값`` **ELSIF** ``조건문`` **THEN** ``결과값`` **ELSE** ``결과값`` **ENDIF**

    - 예시) 점수가 80점 이상이면 1급, 60점 이상이면 2급, 그 아래는 FAIL

    ```sql
    IF SCORE >= 80 THEN '1급' ELSIF SCORE >= 60 THEN '2급' ELSE 'FAIL' ENDIF
    ```



- 형 변환
  - 날짜
    - 오라클은 to_char, mysql은 date_format 사용.
      - **DATE_FORMAT**(``컬럼``, ``format``) 형식으로 사용하고, ``format``에는 무조건 %를 붙인다.
        - %Y = 4자리 연도(2016, 2017,..)
        - %y = 2자리 연도(16, 17,..)
        - %M = January, February,..
        - %m = 00~12
        - %D = 1st, 2nd,... ,31th
        - %d = 01, 02,.. ,31
        - **DATE_FORMAT**(``DATETIME``, ``%Y-%M-%D``)
          - 2021-March-13th
        - **DATE_FORMAT**(``DATETIME``, ``%y-%m-%d``)
          - 21-03-13



##### 루시와 엘라 찾기

- **WHERE** ``NAME`` **in** ``('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')``
  - 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물을 찾으므로 ``in``을 사용하면 여러값을 지정하여 검색할 수 있다.

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```



##### 이름에 el이 들어가는 동물 찾기

- **WHERE** ``ANIMAL_TYPE = 'Dog'`` **AND** ``NAME`` **LIKE** ``'%EL%'``
  - 이름에 'EL'이 들어가고, 개를 찾음

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%EL%'
ORDER BY NAME
```



##### 중성화 여부 파악하기

- **IF** (``SEX_UPON_INTAKE`` **LIKE** ``'%Neutered%'`` **OR** ``SEX_UPON_INTAKE`` **LIKE** ``'%Spayed%'``, ``'O'``, ``'X'``) **AS** ``'중성화'``
  - SEX_UPON_INTAKE가 'Neutered'이거나 'Spayed'면, 중성화이므로 'O' 아닌 경우에는 'X'를 '중성화' 컬럼에 표시
  - 컬럼에 값으로 나타내야 하므로, FROM 앞에 IF를 써서 AS로 컬럼명 표시

```sql
SELECT ANIMAL_ID, NAME, 
IF (SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



##### 오랜 기간 보호한 동물(2)

- ``ANIMAL_OUTS OUTS`` **LEFT OUTER JOIN** ``ANIMAL_INS INS``
  - 입양간 정보를 기준으로 보호소에 있는 정보를 확인
- **ON** ``OUTS.ANIMAL_ID`` = ``INS.ANIMAL_ID``
  - ANIMAL_ID가 외래키이므로 비교
- **ORDER BY** ``OUTS.DATETIME`` - ``INS.DATETIME`` **DESC** **LIMIT** ``2``; 
  - 보호기간이 가장 긴(입양간 날짜-보호 시작일) 보호기간이 긴 순(DESC) 두 마리 조회(LIMIT 2)
  - ORDER BY에 연산자 가능

```sql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC LIMIT 2;
```



- DATETIME에서 DATE로 형 변환
  - 날짜를 2018-01-22 형식으로 나타내야 하므로
    - **DATE_FORMAT**(**DATETIME**, ``'%Y-%m-%d'``)

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



### 종합 문제(서브쿼리)

- 서브쿼리

  - SQL문 안에 또 다른 SQL문이 있음

  - 서브쿼리는 메인쿼리의 컬럼을 사용할 수 있지만, 반대는 안된다.

  - 괄호를 감싸야 한다.

  - 단일 행 또는 복수 행 비교 연산자와 함께 사용 가능

  - ORDER BY 사용불가

  - SELECT, FROM, WHERE, HAVING, ORDER BY, INSERT문의 VALUES, UPDATE문의 SET에서 사용 가능

    - 단일 행 서브쿼리 (=, >, >=, <, <=, <>)

    ```sql
    # 서브쿼리 결과 건수가 반드시 1건 이하
    SELECT *
    FROM PLAYER
    WHERE TEAM_ID = (SELECT TEAM_ID FROM PLAYER WHERE PLAYER_NAME = 'KIM')
    ORDER BY TEAM_NAME
    ```
    
    - 다중 행 서브쿼리 (IN, ALL, ANY, SOME, EXISTS)
    
    ```sql
    # 서브쿼리 결과 건수가 2건 이상
    SELECT *
    FROM PLAYER
    WHERE TEAM_ID IN (SELECT TEAM_ID FROM PLAYER WHERE PLAYER_NAME = 'KIM')
    ORDER BY TEAM_NAME
    ```

    - 다중 컬럼 서브쿼리
    
    ```sql
    # 서브쿼리의 결과로 여러 개의 컬럼이 반환
    SELECT *
    FROM PLAYER
    WHERE (TEAM_ID, HEIGHT) IN (SELECT TEAM_ID FROM PLAYER WHERE PLAYER_NAME = 'KIM')
    ORDER BY TEAM_ID, TEAM_NAME
    ```
    
    - 연관 서브쿼리
      - 서브쿼리 내에 메인쿼리 컬럼이 사용된 서브쿼리
      - 메인쿼리를 먼저 실행 후 서브쿼리에 전달하고 서브쿼리에서 결과 추출 후 메인쿼리에 전달
    
    ```sql
    SELECT T1.X, T1.Y, T1.Z
    FROM A T1
    WHERE T1.Y < (SELECT AVG(T2,Y)
                 FROM A T2
                 WHERE T1.X = T2.X
                 AND T2.Y IS NOT NULL
                 GROUP BY T2.X)
    ```
    
    - EXISTS 서브쿼리
      - 항상 연관 서브쿼리로 사용하며, 조건을 만족하는 결과가 여러 건이라도, 1건만 찾으면 더 이상 검색하지 않는다.
    
    ```sql
    SELECT T1.X, T1.Y, T1.Z
      FROM A T1
     WHERE EXISTS (SELECT 1
                     FROM A T2
                    WHERE T1.X = T2.X
                      AND T2.Y BETWEEN '111' AND  '999');
    ```
    
    - SELECT절 서브쿼리
    
    ```sql
    SELECT X, Y, Z,
           (SELECT AVG(X)   FROM A T2   WHERE T1.X = T2.X) X_AVG
      FROM A T1;
    ```
    
    - FROM절 서브쿼리
    
    ```sql
    SELECT A.Y, B.I, B.J
      FROM A,
           (SELECT X, I, J FROM B WHERE K = '2019') B
     WHERE A.X = B.X;
    ```
    
    




##### 우유와 요거트가 담긴 장바구니

- Milk와 Yogurt를 동시에 구입한 장바구니 출력
- **WHERE** ``NAME`` = ``'Milk' ``
  **AND** ``CART_ID`` **IN** (**SELECT** **DISTINCT** ``CART_ID`` **FROM** ``CART_PRODUCTS`` **WHERE** ``NAME`` = ``'Yogurt'``)
  - Milk를 사고, CART_ID가 (Yogurt를 구입한 CART_ID)와 일치하면 True
  - 쿼리 각각의 데이터에 서브쿼리를 대입하므로 속도가 느림
- **FROM** (**SELECT** `CART_ID` **FROM** `CART_PRODUCTS` **WHERE** `NAME` = '`Milk`') `A`
  **INNER JOIN** (**SELECT** `CART_ID` **FROM** `CART_PRODUCTS` **WHERE** `NAME` = '`Yogurt`') `B` (``A``랑 ``B``는 별칭임) 
  **ON** ``A.CART_ID`` = `B.CART_ID`
  - Yogurt를 산 CART_ID와 Milk를 산 CART_ID가 같은 CART_ID를 출력

```sql
# 서브쿼리
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk' 
AND CART_ID IN (SELECT DISTINCT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt')
ORDER BY CART_ID;

# JOIN
SELECT DISTINCT A.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') A
INNER JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') B
ON A.CART_ID = B.CART_ID;
```



##### 헤비 유저가 소유한 장소

- 공간을 2개 이상 등록한 사람 찾아서 출력 (HOST_ID가 2개 이상 기록되어있는 테이블 확인)
- 중복된 값을 찾는 SQL문
  - **SELECT** 컬럼 **FROM** 테이블 **GROUP BY** 컬럼 **HAVING** count(*) > 1
- **WHERE** `HOST_ID` **IN** (**SELECT** ``HOST_ID`` **FROM** ``PLACES`` **GROUP BY** ``HOST_ID`` **HAVING** ``COUNT(*)`` > ``1``)
  - HOST_ID 그룹 중에 개수가 2개 이상인 HOST_ID를 찾고, WHERE문을 통해 HOST_ID가 들어있는지 확인

```sql
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*) > 1)
ORDER BY ID;
```



## HackerRank

##### Weather Observation Station 2

- station 테이블 중 모든 컬럼의 LAT_N과 LONG_W 필드의 합을 구하는 문제
- 조건 ) 합을 구할 때 소수점이 3번째 자리에서 반올림을 해서 소수점이 2번째 자리까지 나오도록 출력

```sql
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM STATION;
```



##### Weather Observation Station 3

- station 테이블 중 city의 이름을 출력
- 조건 ) id가 **짝수**인 city 명만을 출력 ``MOD(컬럼, 2) = 0``, 홀수면 ``MOD(컬럼, 2) = 1``
- 조건 2 ) city의 이름을 중복 없이 구하기

```sql
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;
```



##### Weather Observation Station 4

- station 테이블 중 city의 개수를 출력
- 조건 ) 개수를 출력할 때 모든 city의 개수와 중복을 제거한 city의 개수를 빼기

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;
```



##### Weather Observation Station 5

- station 테이블 중 도시의 이름과 도시의 이름의 길이를 출력하는데, 도시의 이름의 길이가 가장 짧은 도시의 이름과, 가장 긴 이름의 도시를 출력
- 만약 가장 짧은 도시의 이름이나, 가장 긴 이름의 도시가 복수로 있는 경우에는 알파벳 순서 중 가장 앞에 있는 것을 출력
- 쿼리를 2개로 분리해준다.

```sql
SELECT CITY, LENGTH(CITY) as name_length
FROM STATION
ORDER BY name_length, CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY) as name_length
FROM STATION
ORDER BY name_length DESC CITY
LIMIT 1;
```



###  Regular Expression(정규 표현식)

- . 
  - 점 하나는 문자 하나를 나타냄
  - ex) "..."
    - 문자열의 길이가 세 글자 이상인 것을 찾음
- | (수직선)
  - 또는 (or)로 구분된 문자에 해당하는 문자열을 찾음
  - ex) 데이터 | 데이터
    - '데이터' 또는 '데이타'에 해당하는 문자열을 찾음
- []
  - [] 안에 나열된 패턴에 해당하는 문자열을 찾음
  - ex) "[123]d"
    - 대상 문자열에서 '1d' 또는 '2d' 또는 '3d'인 문자열을 찾음
- ^
  - 시작하는 문자열을 찾음
  - ex) "^안녕"
    - 대상 문자열에서 '안녕'으로 시작하는 문자열을 찾음
- $
  - 끝나는 문자열을 찾음
  - ex) "잘가$"
    - 대상 문자열에서 '잘가'로 끝나는 문자열을 찾음
- +
  - 1회 이상 나타나는 문자
  - ex) "국+"
    - '국'이 1번 이상 등장하는 문자열을 찾음 ('한국', '미역국', '국거리' 등)
- *
  - 0회 이상 나타나는 문자
  - ex) "a*"
    - 'a'가 0번 이상 등장하는 문자열을 찾음 ('b', 'a', 'aa' 등)
- {m,n}
  - m회 이상 n회 이하 반복되는 문자
  - ex) "치{1,2}"
    - '치'가 1회 이상 2회 이하 반복하는 문자열을 찾음 ('치커리', '치카치카' 등)
- [A-z] 또는 [:alpha:]
  - 알파벳 대문자 또는 소문자인 문자열을 찾음
  - ex) "[A-z]+"
    - 대상 문자열에서 알파벳이 한 개 이상인 문자열을 찾음
- [0-9] 또는 [:digit:]
  - 숫자인 문자열을 찾음
  - ex) "^[0-9]+"
    - 한 개 이상의 숫자로 시작하는 문자열을 찾음
- Not
  - [^문자]
    - 괄호 안의 문자를 포함하지 않은 문자열을 찾음
    - ex) "[ ^길로그]"
      - ‘길’ 또는 ‘로’ 또는 ‘그’를 포함하지 않는 문자열을 찾음. ‘길가’, ‘로그’, ‘그리고’ 모두 제외됨.



- 예시)

  - '길' 또는 '로' 또는 '그'가 포함된 문자열을 찾고 싶을 때

  ```sql
  SELECT *
  FROM tbl
  WHERE data REGEXP '길|로|그'
  ```

  - ‘안녕’ 또는 ‘하이’로 시작하는 문자열을 찾고 싶을 때

  ```sql
  SELECT *
  FROM tbl
  WHERE data REGEXP ('^안녕|^하이');
  ```

  - 길이 7글자인 문자열 중 2번째 자리부터 abc를 포함하는 문자열을 찾고 싶을 때

  ```sql
  SELECT *
  FROM tbl
  WHERE data REGEXP ('^.abc...$');
  ```

  - 텍스트와 숫자가 섞여 있는 문자열에서 숫자로만 이루어진 문자열을 찾고 싶을 때

  ```sql
  SELECT *
  FROM tbl
  WHERE data REGEXP ('^[0-9]+$'); 
  -- OR data REGEXP ('^\d$') 
  -- OR data REGEXP ('^[:digit:]$');
  ```




##### Weather Observation Station 6

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 시작하는 도시를 쿼리 하는 문제
- LIKE를 사용해서 모음으로 시작하는 도시의 이름을 쿼리

```sql
# 풀이1
SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE 'A%'
       OR CITY LIKE 'E%'
       OR CITY LIKE 'I%'
       OR CITY LIKE 'O%'
       OR CITY LIKE 'U%'
);

# 풀이2 - 정규식 사용
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou]'
```



##### Weather Observation Station 7

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 끝나는 도시를 쿼리 하는 문제
- 정규식을 사용해서 풀이

```sql
SELECT DISTINCT CITY 
FROM STATION
WHERE CITY REGEXP '[aeiou]$';
```



##### Weather Observation Station 8

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 시작하면서, 모음으로 끝나는 도시를 쿼리 하는 문제
- 정규식을 사용해서 풀이
- .는 가운데 무슨 글자든지 상관없이 하나임
- *은 앞의 글자가 0개 이상있는 경우 (%)
- .*는 어떠한 글자든지 (0개 이상)

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
```



##### Weather Observation Station 9

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 시작하지 않는 도시의 이름을 쿼리 하는 문제
- 정규식을 사용해서 풀이

```sql
SELECT DISTINCT CITY 
FROM STATION    
WHERE CITY REGEXP '^[^aeiou]';
```



##### Weather Observation Station 10

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 끝나지 않는 도시의 이름을 쿼리 하는 문제
- 정규식을 사용해서 풀이

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[^aeiou]$';
```



##### Weather Observation Station 11

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 시작하지 않거나 모음으로 끝나지 않는 도시의 이름을 쿼리 하는 문제
- 정규식을 사용해서 풀이

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiou]|[^aeiou]$';
```



##### Weather Observation Station 12

- station 테이블 중 도시의 이름 중에서 모음(a, e, i, o, u)으로 시작하지 않고 모음으로 끝나지 않는 도시의 이름을 쿼리 하는 문제
- 정규식을 사용해서 풀이

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiou].*[^aeiou]$';
```



##### Weather Observation Station 13

- station 테이블 중 lat_n 칼럼의 모든 합을 구하는데 아래의 조건을 만족한 칼럼에서만 합을 구함
- 또한 합을 구한 뒤에 소수점 4자리까지만 출력되도록 버림(TRUNCATE)을 해서 쿼리 하는 문제
- lat_n이 38.7880보다 크고, 137.2345보다 작은 경우

```sql
SELECT TRUNCATE(SUM(LAT_N), 4) FROM STATION WHERE LAT_N BETWEEN 38.7880 AND 137.2345;
```



##### Weather Observation Station 14

- station 테이블 중 lat_n 칼럼 중 가장 큰 수를 출력
- lat_n이 137.2345보다 작은 숫자 중에서 가장 큰 수
- 구한 수에서 소수점 4자리까지만 출력되도록 버림(TRUNCATE)

```sql
SELECT TRUNCATE(MAX(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345;
```



##### Weather Observation Station 15

- station 테이블 중 특정 조건에 만족하는 long_w를 구하는 문제
- lat_n이 137.2345보다 작은 숫자 중에서 가장 큰 수(largest) -> 내림차순(큰 수부터), LIMIT 1
- 구한 숫자 중에서 소수점 4개까지만 출력 되게 버림을 해야 한다.

```sql
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;
```



##### Weather Observation Station 16

- station 테이블에서 lat_n 컬럼 중 조건을 만족하는 컬럼 중 가장 작은 수를 출력하는 쿼리문을 작성하는 문제
- lat_n이 38.7780보다 크고, 구한 숫자 중에서 소수점 4개 까지만 출력 되게 반올림을 해야 한다.

```sql
# 풀이1
SELECT ROUND(LAT_N, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;

# 풀이2
SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780;
```



##### Weather Observation Station 17

- station 테이블에서 long_w 칼럼 중 조건을 만족하는 칼럼을 쿼리 하는 문제
- lat_n이 38.7780보다 큰 수 중에 lat_n이 가장 작은 컬럼의 long_w를 소수점 4자리까지 출력

```sql
# 풀이1
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;

# 풀이2
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);
```



##### Weather Observation Station 18

- a = lat_n의 최솟값, b = long_w의 최솟값, c = lat_n의 최댓값, d = long_w의 최댓값
- 맨하탄 거리 공식 = | a - c | + | b - d |
- 소수점 4자리까지만 출력
- MIN, MAX, ABS, ROUND 사용

```sql
SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4)
FROM STATION;
```



##### Higher Than 75 Marks

- Students 테이블에서 Marks가 75가 넘는 사람의 이름을 이름의 마지막에서 3번째 문자 기준으로 오름차순 정렬하고, 두번째는 ID를 오름차순으로 정렬하여 나타내기
- 문자열 자르기
  - RIGHT('문자열', 길이)
    - RIGHT('abcde', 2) = 'de'
  - LEFT('문자열', 길이)
    - LEFT('abcde', 2) = 'ab'

```sql
SELECT Name 
FROM STUDENTS 
WHERE Marks > 75 
ORDER BY RIGHT(Name, 3), ID;
```



##### Population Census

- CITY 테이블과 COUNTRY 테이블을 이용해서 COUNTRY.CONTINENT가 'Asia'인 모든 CITY의 인구(POPULATION)의 합을 구하기
- CITY.COUNTRYCODE와 COUNTRY.CODE는 외래키
- JOIN하여 CONTINENT가 'Asia'인 것 찾아서 출력하면 끝

```sql
SELECT SUM(CITY.POPULATION)
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia'
```



##### African Cities

- CITY 테이블과 COUNTRY 테이블을 이용해서 COUNTRY.CONTINENT가 'Africa'인 모든 CITY의 이름을 출력
- CITY.COUNTRYCODE와 COUNTRY.CODE는 외래키
- JOIN하여 CONTINENT가 'Asia'인 것 찾아서 출력하면 끝

```sql
SELECT CITY.NAME
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa'
```



##### Average Population of Each Continent

- CITY 테이블과 COUNTRY 테이블을 이용해서 COUNTRY.CONTINENT마다 CITY.POPULATION의 평균을 가장 근접한 정수로 출력(소수점은 버리고 정수로만 출력)
- CONTINENT마다 CITY의 평균을 출력해야하므로 GROUP BY를 한다.
- FLOOR는 소수점 첫째 자리에서 버림하는 함수. 가장 근접한 정수를 찾는 것
- CEIL은 소수점 첫째 자리에서 올림하는 함수. 가장 근접한 큰 정수를 찾는 것

```sql
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY INNER JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT
```



##### The Report

- Students 테이블과 Grades 테이블을 이용해서 Name, Grade, Marks를 출력하기
- Name은 Student의 이름이고, Grade가 8이상인 경우만 출력하고, 그렇지 않으면 NULL로 출력
- Students의 Marks는 Grade의 Min_Mark와 Max_Mark 사이로 찾아서 Grade를 판별
- Grade는 내림차순, Name과 Marks는 오름차순으로 정렬

```sql
SELECT IF(G.Grade > 7, S.Name, 'NULL'), G.Grade, S.Marks
FROM Students AS S 
INNER JOIN Grades AS G 
ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC, S.Name, S.Marks 
```



##### Top Competitors

- 문제 : 코테 제출자 중 2개 이상의 challenge에서 full score를 받은 hackers들의 id와 name을 challenge 개수를 기준으로 정렬하고 full score를 받은 hackers들의 challenge 개수가 동일하다면, hacker_id를 기준으로 오름차순 정렬해라.
- full score는 Submissions(S)의 score와 Difficulty(D)의 score가 일치해야함.
- Hackers(H) 테이블, Difficulty(D) 테이블, Challenges(C) 테이블, Submissions(S) 테이블을 JOIN
- S의 score와 D의 score를 비교하려면 먼저 C테이블과 challenge_id로 JOIN을 맺는다.
- C테이블은 D테이블과 difficulty_level을 통해 JOIN을 맺는다.
- 그리고 S테이블은 H테이블과 hacker_id를 통해 JOIN을 맺는다.
- 조인을 잘해야한다!!

```sql
SELECT H.hacker_id, H.name
FROM Submissions S
    INNER JOIN Challenges C ON S.challenge_id = C.challenge_id
    INNER JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
    INNER JOIN Hackers H ON S.hacker_id = H.hacker_id
WHERE S.score = D.score	# S(제출) score와 D(난이도) score가 동일하다면 full score
GROUP BY H.hacker_id, H.name	# hacker_id와 name을 묶는다.
HAVING COUNT(S.challenge_id) > 1	# 제출한 challenge 개수를 세고, 2개 이상만 추출 
ORDER BY COUNT(S.challenge_id) DESC, H.hacker_id;	# challenge 개수를 기준으로 내림차순 정렬, 동일하면 hacker_id 기준 오름차순 정렬
```



##### Ollivander's Inventory

- 문제 : non_evil(is_evil=0)이면서, 높은 Power와 Age를 가진 지팡이를 사기 위해 필요한 최소한의 gold galleons(coins_needed)를 구하고, 정렬은 power 기준으로 내림차순 정렬하고, 동일 power가 있다면 age를 기준으로 내림차순하여 id, age, coins_needed, power 출력해라.
- JOIN + 서브쿼리 문제(연관 서브쿼리)
- Wands 테이블과 Wands_Property 테이블을 code를 통해 JOIN한다.
- non_evil(is_evil=0)이어야 하고, coins_needed의 최소치를 구해야 하므로 WHERE 절에 서브쿼리를 사용한다.
- 서브쿼리에서 다시 Wands 테이블과 Wands_Property 테이블을 code를 통해 JOIN하고, 별칭은 메인쿼리 JOIN과 다르게 한다.
- 서브쿼리의 WHERE 또한, non_evil(is_evil=0)이어야 하고, 메인쿼리에서 JOIN한 power, age와 서브쿼리로 JOIN한 power, age를 각각 같게 한다.

```sql
SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W 
INNER JOIN Wands_Property P ON W.code = P.code
WHERE P.is_evil = 0 
AND W.coins_needed = (SELECT MIN(coins_needed) 
                      FROM Wands W1
                     INNER JOIN Wands_Property P1 ON W1.code = P1.code
                     WHERE P1.is_evil = 0
                     AND W1.power = W.power
                     AND P1.age = P.age)
ORDER BY W.power DESC, P.age DESC
```



##### Contest Leaderboard

- hacker의 total score란, 그 hacker가 푼 모든 문제들에 대한 score의 최댓값의 합을 의미한다. 이 때 hacker_id, name, total_score를 출력하는데 1차정렬 기준은 total_score를 내림차순, 2차정렬 기준은 hacker_id 오름차순으로 정렬해라. (단, 결과값에서 total score가 0인 데이터들은 제외)
- 문제(challenge_id)
- (**SELECT** ``hacker_id``, ``challenge_id``, ``MAX(score)`` **AS** ``max_score`` **FROM** ``Submissions`` **GROUP BY** ``hacker_id``, ``challenge_id``) ``sub1``
  - hacker_id가 풀은 challenge_id 중 가장 높은 score를 찾기 위해 만든 서브쿼리를 그룹핑(2단계-제일 내부)
- (**SELECT** ``sub1.hacker_id``, ``SUM(max_score)`` **AS** ``total_score`` **FROM**  sub1 **GROUP BY** ``sub1.hacker_id`` **HAVING** ``total_score`` != ``0`` ) ``sub2``
  - 가장 높은 score들로 total_score를 만들기 위해 hacker_id 기준으로 만든 서브쿼리를 그룹핑(1단계) (단, total_score가 0인 것은 제외)
- (**SELECT** ``H.hacker_id``, ``H.name``, ``sub2.total_score``) **FROM** ``sub2`` **INNER JOIN** ``Hackers`` ``H`` **ON** ``sub2.hacker_id`` = ``H.hacker_id`` **ORDER BY** ``sub2.total_score`` **DESC**, ``H.hacker_id``
  - hacker_id, name, total_score를 나타내기 위해 Hackers 테이블과 sub2 테이블을 JOIN시키고, 정렬기준에 따라 출력시켜준다.
- 먼저 구해야하는 것을 유도해서 구하고, 그다음 과정을 구하고 하는식으로 서브쿼리를 통해 직관적으로 풀면 된다.

```sql
# 풀이1
SELECT H.hacker_id, H.name, sub2.total_score
FROM (SELECT sub1.hacker_id, SUM(max_score) AS total_score
     FROM (SELECT hacker_id, challenge_id, MAX(score) AS max_score
            FROM Submissions
            GROUP BY hacker_id, challenge_id) sub1
    GROUP BY sub1.hacker_id
    HAVING total_score != 0) sub2
INNER JOIN Hackers H ON sub2.hacker_id = H.hacker_id
ORDER BY sub2.total_score DESC, H.hacker_id

# 풀이2
SELECT sub1.hacker_id, H.name, SUM(sub1.MAX_Score) AS total_score
FROM 
	(SELECT hacker_id, challenge_id, MAX(score) AS MAX_score
    FROM submissions
    GROUP BY hacker_id, challenge_id) sub1
INNER JOIN Hackers H 
ON sub1.hacker_id = H.hacker_id
GROUP BY sub1.hacker_id, H.name
HAVING total_score > 0
ORDER BY total_score DESC, sub1.hacker_id
```


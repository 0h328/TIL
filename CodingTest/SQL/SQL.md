# SQL(programmers)

### SELECT

- 모든 레코드 조회하기

```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```



- 역순 정렬하기

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;
```



- 아픈 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION='Sick';
```



- 어린 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION NOT IN('Aged') ORDER BY ANIMAL_ID;

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID;
```



- 동물의 아이디와 이름

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```



- 여러 기준으로 정렬하기

```sql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;
```



- 상위 n개 레코드

```sql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1;
```





### SUM, MAX, MIN

- 최댓값 구하기

```sql
SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;

SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS;
```



- 최솟값 구하기

```sql
SELECT DATETIME AS 시간 FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;

SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS;
```



- 동물 수 구하기

```sql
SELECT COUNT(*) AS COUNT FROM ANIMAL_INS;
```



- 중복 제거하기

```sql
SELECT COUNT(DISTINCT NAME) AS COUNT FROM ANIMAL_INS;

SELECT COUNT(DISTINCT NAME) AS count FROM ANIMAL_INS WHERE NAME IS NOT NULL;

SELECT COUNT(DISTINCT NAME) AS count FROM ANIMAL_INS;
```



### GROUP BY

- **SELECT** ``컬럼A``, ``컬럼B`` **FROM** ``테이블`` **GROUP BY** ``컬럼A``
  - 그룹화하는 컬럼은 반드시 SELECT로 조회해야함.



- 고양이와 개는 몇 마리 있을까

```sql
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;
```



- 동명 동물 수 찾기

```sql
SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME;
```



- 입양 시각 구하기(1)

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT FROM ANIMAL_OUTS GROUP BY HOUR HAVING HOUR BETWEEN 9 AND 19 ORDER BY HOUR(DATETIME);
```



- 입양 시각 구하기(2)

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

- 이름이 없는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL;

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY ANIMAL_ID;
```



- 이름이 있는 동물의 아이디

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL;

SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID;
```



- NULL 처리하기

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE FROM ANIMAL_INS;

SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```





### JOIN

- 두 테이블의 데이터를 일정한 조건에 의해 연결하여 마치 하나의 테이블처럼 만드는 것
  - **INNER JOIN**과 **LEFT OUTER JOIN**이 많이 쓰임
    - **LEFT OUTER JOIN**
      - 왼쪽 테이블 기준으로 조건에 맞는 오른쪽 테이블의 데이터를 가져옴
      - 없으면 NULL
  - **(LEFT) JOIN** vs **(LEFT) OUTER JOIN**
    - 단일 **JOIN**은 빈 값은 안가져오고, **OUTER JOIN**은 빈 값까지 가져온다.



- 없어진 기록 찾기
  - **SELECT** ``OUTS.ANIMAL_ID``, ``OUTS.NAME``
    - 왼쪽 데이터를 기준으로 ANIMAL_ID와 NAME 데이터 조회
  - **FROM** ``ANIMAL_OUTS OUTS`` **LEFT OUTER JOIN** ``ANIMAL_INS INS``
    - 입양을 간 기록이 존재하므로, 존재하는 기록을 바탕으로 존재하지 않는 데이터를 조회하기 위함
  - **ON** ``OUTS.ANIMAL_ID`` = ``INS.ANIMAL_ID``
    - ANIMAL_ID를 기준으로 데이터 유무 차이를 판단함
  - **WHERE** INS.ANIMAL_ID **is NULL**
    - JOIN 이후에 왼쪽 테이블 기준으로 오른쪽 테이블의 데이터가 없으면 NULL이 표시되므로 is NULL 조건 사용
  - **ORDER BY** OUTS.ANIMAL_ID
    - ID 순으로 조회

```sql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS 
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID
```



- 있었는데요 없었습니다
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
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME

# JOIN 미사용
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID and INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME
```



- 오랜 기간 보호한 동물(1)
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
SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME LIMIT 3;
```



- 보호소에서 중성화한 동물
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
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS LEFT OUTER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME
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
        - **DATE_FORMAT**(``DATETIME``, ``%y-%M-%D``)
          - 21-03-13



- 루시와 엘라 찾기
  - **WHERE** ``NAME`` **in** ``('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')``
    - 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물을 찾으므로 ``in``을 사용하면 여러값을 지정하여 검색할 수 있다.

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```



- 이름에 el이 들어가는 동물 찾기
  - **WHERE** ``ANIMAL_TYPE = 'Dog'`` **AND** ``NAME`` **LIKE** ``'%EL%'``
    - 이름에 'EL'이 들어가고, 개를 찾음

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND NAME LIKE '%EL%'
ORDER BY NAME
```



- 중성화 여부 파악하기
  - **IF** (``SEX_UPON_INTAKE`` **LIKE** ``'%Neutered%'`` **OR** ``SEX_UPON_INTAKE`` **LIKE** ``'%Spayed%'``, ``'O'``, ``'X'``) **AS** ``'중성화'``
    - SEX_UPON_INTAKE가 'Neutered'이거나 'Spayed'면, 중성화이므로 'O' 아닌 경우에는 'X'를 '중성화' 컬럼에 표시
    - 컬럼에 값으로 나타내야 하므로, FROM 앞에 IF를 써서 AS로 컬럼명 표시

```sql
SELECT ANIMAL_ID, NAME, 
IF (SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```



- 오랜 기간 보호한 동물(2)
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


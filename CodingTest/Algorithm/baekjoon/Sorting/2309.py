d = []                                      # 입력값 저장 list

for _ in range(9):                          # 난쟁이 9명 반복
    height = int(input())                   # 키(height) 변수에 입력
    d.append(height)                        # 생성 list에 추가

not_d1 = 0                                  # 거짓난쟁이1 변수 설정 및 초기화
not_d2 = 0                                  # 거짓난쟁이2 변수 설정 및 초기화

total = 0                                   # 난쟁이 키 합을 구하기 위한 total 변수 설정
for i in d:
    total += i

for i in range(len(d)-1):                   # index 0부터 비교하기 위해 범위 설정
    for j in range(i+1, len(d)):            # index 0과 그다음 index를 비교하기 위한 범위 설정
        if total - (d[i] + d[j]) == 100:    # d의 총합 - 거짓난쟁이의 키 합 = 100 되야함.     
            not_d1 = d[i]                   # if 조건문에 해당되면 거짓난쟁이1,2의 키 갱신      
            not_d2 = d[j]

d.remove(not_d1)                            # 저장 list에서 거짓난쟁이1,2의 키 제거
d.remove(not_d2)
d.sort()                                    # 오름차순으로 정렬

for i in d:                                 # 갱신된 d list를 반복
    print(i)                                # 출력예시에 따라 출력
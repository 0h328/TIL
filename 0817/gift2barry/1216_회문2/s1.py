import sys
sys.stdin = open('input.txt')

# thought process: 소요시간 5분
# 가장 긴 회문을 찾는 문제이다.
# 스텝 두가지로 나누자: 반복작업 할 영역, 그리고 확인 할 영역
# 반복작업: 반복작업 범위를 지정하고 고지식 알고리즘으로 루프 돌린다
# 확인작업: 반대로 뒤바꾼거랑 동일하면 루프 그만하고 프린트

int(input()) + 1

row_arr = [input() for _ in range(100)]  # 행 알파벳들 리스트에 저장
col_arr = list(zip(*row_arr))  # 열 알파벳들 튜플로 반환

N = 100                        # 전체 문자열 길이
T = 100                        # 텍스트열 길이
maxValue = 0                   # 최장 회문길이 변수
# 행 최대 회문 길이 계산
# for i in range(N):
#     cnt = 0
#     for j in range(0,T-i):
#         if row_arr[i][j] == row_arr[i][-1-j]:
#             if row_arr[i][j:-1-j] == row_arr[i][j:-1-j][::-1]:
#                 cnt = len(row_arr[i][j:-1-j])
#     if cnt > maxValue:
#         maxValue = cnt
# print(maxValue)

for i in range(N):
    for j in range(T-i, 0, -1):
        if row_arr[i][i] == row_arr[i][j]:
            if row_arr[i][i:j] == row_arr[i][i:j][::-1]:
                maxValue = row_arr[i][i:j]
                print(maxValue)

# 열 최대 회문 길이 계산

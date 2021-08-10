import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
# print(N, M)

# 이차원 리스트 받기
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

#1.  행 우선 순회
for i in range(N):
    for j in range(M):
        arr_row = arr[i][j]
        print(arr_row)

#2.  열 우선 순회
for j in range(M):
    for i in range(N):
        arr_col = arr[i][j]
        print(arr_col)

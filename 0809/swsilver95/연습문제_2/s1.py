import sys
sys.stdin = open('input.txt')

# 행/열의 길이 받기
N, M = map(int, input().split())

# 이차원 리스트 받기
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(arr)

# 1. 행 우선 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j])


# 2. 열 우선 순회
for i in range(M):
    for j in range(N):
        print(arr[j][i])
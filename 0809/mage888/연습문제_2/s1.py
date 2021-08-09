import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
print(N, M)

# 이차원 리스트 받기
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

#1. 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr)+1):
        print(arr[i][j])

#2. 열 우선 순회
for i in range(len(arr)+1):
    for j in range(len(arr)):
        print(arr[j][i])


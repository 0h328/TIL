import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
print(N, M)

# 이차원 리스트 받기
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 행 우선 순회
for n in range(N): # 행을 고정으로 두고
    for m in range(M): # 우선 해당 행의 열을 다 뽑음
        print(arr[n][m])

# 2. 열 우선 순회
for m in range(M): # 열을 고정으로 두고
    for n in range(N): # 해당 열의 행을 다 뽑음
        print(arr[n][m])
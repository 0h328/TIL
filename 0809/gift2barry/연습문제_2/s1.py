import sys
sys.stdin = open('input.txt')

# 행 / 열 길이 받기
N, M = map(int, input().split())
print(N, M)


# 2차원 리스트 받기
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)


# 1. 행 우선 순회

# 2. 열 우선 순회
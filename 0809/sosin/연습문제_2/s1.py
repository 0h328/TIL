import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 행 우선 순회
for row in arr:
    for e in row:
        print(e, end=' ')
    print()

# 2. 열 우선 순회
for col in zip(*arr):
    for e in col:
        print(e, end=' ')
    print()

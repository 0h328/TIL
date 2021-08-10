import sys
sys.stdin = open('input.txt')

# 행 / 열의 길이 받기
N, M = map(int, input().split())
# print(N, M)

# 이차원 리스트 받기
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

#1. 행 우선 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
"""
0 1 2 3 4 5 6 7 8 9 10 11
"""

#2. 열 우선 순회
for j in range(M):
    for i in range(N):
        print(arr[i][j], end=' ')

"""
0 4 8 1 5 9 2 6 10 3 7 11
"""

#3. 역-행 우선순회
for i in range(N):
    # index 0까지(-1 + 1)
    for j in range(M-1, -1, -1):
        print(arr[i][j], end=' ')
"""
3 2 1 0 7 6 5 4 11 10 9 8
"""

#4. 역-열 우선순회
for i in range(M-1, -1, -1):
    for j in range(N):
        print(arr[j][i], end=' ')
"""
3 7 11 2 6 10 1 5 9 0 4 8
"""

#5. 지그재그 순회
for i in range(N):
    for j in range(M):
        # (i % 2)는 0+짝 vs 홀수 열에 대한 구분
        # 애초에 0 + 짝수열은 수행되지 않음
        print(arr[i][j + (M-1-2*j) * (i%2)], end=' ')
"""
0 1 2 3 7 6 5 4 8 9 10 11
"""
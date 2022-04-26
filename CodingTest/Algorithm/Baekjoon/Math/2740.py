import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr_A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
arr_B = [list(map(int, input().split())) for _ in range(M)]

# (3x2) x (2x3) => (3x3) 행렬
# (NxM) x (MxK) => (NxK) 행렬
answer = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            answer[i][j] += arr_A[i][k] * arr_B[k][j]

for ans in answer:
    for a in ans:
        print(a, end=' ')
    print()

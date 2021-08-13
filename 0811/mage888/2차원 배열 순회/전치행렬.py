import sys
sys.stdin = open('input.txt')

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i < j:
            A[i][j], A[j][i] = A[j][i], A[i][j]
            # A[i][j] = A[j][i] # 역슬래쉬 윗 부분은 바뀌게됨.

print(A)


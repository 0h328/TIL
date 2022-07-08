import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
cnt = 0

def flip(x, y):

    for a in range(x, x+3):
        for b in range(y, y+3):
            A[a][b] = 1 - A[a][b]


for i in range(N-2):      # 줄바꿈 가능 횟수
    for j in range(M-2):  # 가로 줄 이동 가능 횟수
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1
        if A == B:
            break

    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)
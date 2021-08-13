import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

i, j = 1, 1

# 위, 아래, 왼, 오
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]

    # 벽 안으로 들어오는 조건
    if (0 <= ni < N) and (0 <= nj < N):
        print(data[ni][nj])

    # 벽 밖으로 나가면 그냥 continue
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
        continue
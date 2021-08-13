import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 위, 아래, 왼, 오
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    total = 0

    for i in range(N): # 모든 기준점에 대해 실행: i, j 루프 돌기
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                # 벽 안으로 들어오는 조건
                if (0 <= ni < N) and (0 <= nj < N):
                    total += abs(data[ni][nj] - data[i][j])

                # 벽 밖으로 나가면 그냥 continue
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue

    print('#{} {}'.format(t, total))
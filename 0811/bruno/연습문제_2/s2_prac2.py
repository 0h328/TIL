import sys
sys.stdin = open('input2.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

tc = int(input())
for i in range(1, tc+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N):
        for c in range(N):
            for k in range(N-1):
                nr = r + dr[k]
                nc = c + dc[k]
                if (0 <= nr < N) and (0 <= nc < N):
                    ans += abs(data[r][c] - data[nr][nc])

    print('#{} {}'.format(i, ans))

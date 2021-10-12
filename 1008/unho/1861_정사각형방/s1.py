import sys
from pprint import pprint
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


def dfs(y, x):
    if dp[y][x] > -1:
        return dp[y][x]

    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N and board[y][x] + 1 == board[r][c]:
            dp[y][x] = 1 + dfs(r, c)
            return dp[y][x]

    dp[y][x] = 0
    return dp[y][x]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * N for _ in range(N)]
    tmp_answer = 0
    tmp_answer_li = []

    for i in range(N):
        for j in range(N):
            ans = dfs(i, j)
            if tmp_answer <= ans + 1:
                if tmp_answer < ans + 1:
                    tmp_answer = ans + 1
                    tmp_answer_li.clear()
                tmp_answer_li.append(board[i][j])

    answer.append('#{} {} {}'.format(tc, min(tmp_answer_li), tmp_answer))

print(*answer, sep='\n')
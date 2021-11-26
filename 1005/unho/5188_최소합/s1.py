"""
브루트포스 / DFS
"""

import sys
sys.stdin = open('input.txt')


def dfs(y, x, ans):                         # DFS
    global answer

    if y == N-1 and x == N-1:               # 오른쪽 끝에 도달시
        if answer > ans:                    # 최솟값이 된다면 새로 저장
            answer = ans
        return
    elif answer <= ans:                     # 중간에 최솟값을 넘어서면 그냥 종료
        return

    for k in range(2):                      # 오른쪽과 아래로만 탐색
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N:       # 범위내면 재귀
            dfs(r, c, ans + board[r][c])

dr = [1, 0]
dc = [0, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e10
    
    dfs(0, 0, board[0][0])

    print('#{} {}'.format(tc, answer))    
""" 완전탐색 / DFS """

import sys
sys.stdin = open('input.txt')


def dfs(idx, ans):
    global answer

    if sum(visited) >= N-1:
        ans += board[idx][1]            # 1번 구역은 마지막에 도착하여야하므로
        if answer > ans:
            answer = ans
        return
    elif ans >= answer:
        return
    
    for i in range(2, N+1):                 # 모든 경우 탐색
        if not visited[i] and idx != i:     # 제자리는 갈 필요 없음
            visited[i] = 1
            dfs(i, ans + board[idx][i])
            visited[i] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    answer = 1e10
    
    dfs(1, 0)

    print('#{} {}'.format(tc, answer))
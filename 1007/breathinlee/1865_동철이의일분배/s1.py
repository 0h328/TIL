"""
“주어진 일이 모두 성공할 확률”의 최댓값
모든 일을 성공할 확률이 최대가 되고 그 확률은 (0.13*0.7*1.0)*100 = 9.1%
"""
def dfs(idx, total):
    global max_result

    if idx == N:
        if max_result < total:
            max_result = total
            return

    if max_result >= total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, total*probability[idx][i]*(100**(-1)))
            visited[i] = 0

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    probability = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0

    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, max_result*100))
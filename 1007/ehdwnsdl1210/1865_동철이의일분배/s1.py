'''
N명의 직원 / 해야할 일이 N개
공평하게 일을 하나씩 배분
직원들의 번호가 1부터 N까지 / 해야 할 일에도 번호가 1부터 N까지
i번 직원이 j번 일을 하면 성공할 확률이 Pi,j
주어진 일이 모두 성공할 확률의 최댓값?
'''

def DFS(n, total):
    global max_result

    if total <= max_result:
        return

    if n == N:
        max_result = total

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            DFS(n + 1, total * percentage[n][i] / 100)
            visited[i] = 0

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    percentage = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0

    DFS(0, 1)

    print('#{} {:.6f}'.format(tc, max_result * 100))
"""
1. 1개의 셀에는 1개의 코어 혹은 전선 올 수 있음
2. 가장 자리에 전원이 흐르므로 코어에 연결된 전선은 가장 자리에 닿아야 함
3. 이 때, 각 코어 간 연결된 전선은 교차 불가
4. 코어가 가장자리에 있을 경우 이미 전선 연결된 것으로 간주(전선 필요X)
=> 최대한 많은 코어에 전원을 연결했을 때, 전선 길이의 합 구해라!!
(여러 방법 있을 경우, 전선 길이의 합 중 최소 출력할 것)

=> N*N 크기 (7 <= N <= 12) / 1 <= 코어 <= 12 / 최대한 많은 코어에 전원 연결해도, 전원이 연결되지 않는 코어 존재 할 수 있음
핵심!!!! 최대한 많은 코어 사용할 것
0은 빈 cell, 1은 core

생각해보자.
1. 코어가 가장 자리에 있는 경우 (row = 0 / row = N-1 / col = 0 / col = 7) => 전선 연결 x
2. 가장 자리에 있지 않은 코어의 좌표를 저장해놓고 for문을 돌리면서 bfs탐색하면 되지 않을까
3. bfs안에서 다른 전선과 만나거나 다른 코어와 만나거나 가장자리에 닿을 때 종료 (전선이 놓인 셀을 2라고 해보자..)
4. max값 저장해놓고 계속 비교하며 갱신하기
5. 더 고려해야 할 조건은 뭘까..
"""

def bfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]




import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    # visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(N):
        for col in range(N):
            if board[row][col]:
                if row != 0 and col != 0:       # 가장 자리에 있는 코어 제외
                    core.append((row, col))

    for core in cores:
        r, c = core[0], core[1]
        bfs(r, c)



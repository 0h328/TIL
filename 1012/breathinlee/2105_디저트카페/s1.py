"""
대각선 방향으로 움직일 수 있음 => direction = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
사각형 모양을 그리며 출발한 카페로 돌아와야 함 + 범위 내 존재해야
움직일 곳이 같은 숫자이면 갈 수 없음
왔던 길 다시 돌아가는 것 x (visited 체크) + 최소 1번 이상 움직여야(갈 곳이 없다면 -1)
디저트를 가장 많이 먹을 수 있는 경로 찾기(디저트 수 출력) / 디저트 먹을 수 없을 경우 -1

조건
1. 범위 내 존재 0 <= nr = r + direction[k][0], nc = c + direction[k][1] < N
2. 방문한 곳 (r, C)에 대하여 visited[r][c] = 1
3. 방문할 곳 (nr, nc)에 대하여 cafe[nr][nc] != cafe[r][c]
4. max_cnt 설정하여 계속 갱신
5. 처음 시작점 => start_point에 담자
6. dfs 인자로는 좌표, 방향 외에 뭐가 들어와야 할까
"""

# 미완성

def find_route(r, c, d):
    dessert = [cafe[r][c]]
    nr = r + direction[d][0]
    nc = c + direction[d][1]

    if (nr, nc) == start_point[0]:
        return

    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
        if cafe[nr][nc] not in dessert:
            dessert.append(cafe[nr][nc])
            visited[nr][nc] = 1
            find_route(nr, nc, d)
            dessert.remove(cafe[nr][nc])
            # visited[nr][nc] = 0
            find_route(nr, nc, (d+1) % 4)

    return len(dessert) + 1


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_cnt = -1
    for i in range(N-2):
        for j in range(1, N-1):
            start_point = [(i, j)]           # 처음 출발점 저장
            max_cnt = max(max_cnt, find_route(i, j, 0))

    print('#{} {}'.format(tc, max_cnt))
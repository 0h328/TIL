import sys
import pprint
sys.stdin = open('input.txt')

# 소요시간 1시간 2분

# thought process: 7분 53 초
# 인접행렬 생성
# visited 생성
# 모든 인접행렬 처음부터 방문
# 배추가 있고 미방문인 지점 발견하면 dfs or bfs함수 접근
# 모든 연결된 지점을 방문하며 visited = 1 로 체크
# 연결 지점은 우하좌상 방향델타값 활용
# dfs 함수를 다 돌때마다 지렁이 개수 +1
# 다시 모든 인접행렬 처음부터 방문

#    우 하  좌  상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    global cnt
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        cnt += 1
        if 0 < nr <= V and 0 < nc <= H:

            if G[nr][nc] == 1 and not visited[nr][nc]:
                dfs(nr, nc)
    return


for tc in range(1, int(input())+1):
    H, V, K = map(int, input().split())     # 가로, 세로, 심어진 배추 개수(node)
    tmp = [list(map(int, input().split())) for _ in range(K)]
    G = [[0] * (H+1) for _ in range(V+1)]
    visited = [[0] * (H+1) for _ in range(V+1)]
    ans = 0
    cnt = 0
    for i in range(K):
        G[tmp[i][1]+1][tmp[i][0]+1] = 1
    for j in range(1, V+1):
        for k in range(1, H+1):
            if G[j][k] == 1 and not visited[j][k]:
                dfs(j, k)
                ans += 1
    print('#{}번 정답: {}'.format(tc, ans))
    print('재귀 횟수: {}'.format(cnt))

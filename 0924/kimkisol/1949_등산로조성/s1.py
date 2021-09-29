import sys

sys.stdin = open('input.txt')


# 산깎기는 나중에 적용
def dfs(r, c, l, chance):  # r: 행, c: 열, l: 등산로 길이, chance: 깎을 기회
    global result, cnt

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not visited[nr][nc] and 0 <= m[nr][nc]:
            if m[nr][nc] < m[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, l + 1, chance)
                visited[nr][nc] = 0
            elif chance and m[nr][nc] - K < m[r][c]:  # 깎을 기회가 있고, 현재에서 K만큼 깎은게 이전꺼보다 낮을 경우만
                temp = m[nr][nc]  # 깎기 전
                m[nr][nc] = m[r][c] - 1  # 깎기
                visited[nr][nc] = 1
                dfs(nr, nc, l + 1, chance - 1)
                visited[nr][nc] = 0
                m[nr][nc] = temp  # 깎기 전으로 되돌려주기

    cnt += 1
    if l > result:
        result = l


T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())  # N: 지도 한변 길이, K: 최대 공사 가능 깊이
    m = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    result = 1
    cnt = 0

    # 가장 높은 봉우리 높이 구하기
    max_h = max(sum(m, []))

    # 시작점 구하기
    start = []
    for i in range(N + 2):
        for j in range(N + 2):
            if m[i][j] == max_h:
                start.append((i, j))

    for s in start:
        visited[s[0]][s[1]] = 1
        dfs(s[0], s[1], 1, 1)
        visited[s[0]][s[1]] = 0

    print('#{} {}'.format(t, result))
    print(cnt)

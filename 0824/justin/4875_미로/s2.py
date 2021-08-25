def dfs(r, c):
    global ans
    data[r][c] = 'visit'                        # 첫 출발 지점을 방문 처리하고 시작 (더미 문자열)
    for i in range(4):                          # 만약 ans가 1로 바뀌었다면 함수 종료
        if ans: return
        nr = r + dr[i]                          # 이동
        nc = c + dc[i]
        if nr < 0 or nr == N: continue          # 범위 체크
        if nc < 0 or nc == N: continue
        if data[nr][nc] == 'visit': continue    # 방문 했던 곳 체크
        if data[nr][nc] == 1: continue          # 벽 체크
        if data[nr][nc] == 3:                   # 도착지면
            ans = 1                             # 1로 바꾸고 종료
            return
        dfs(nr, nc)                             # 미로를 탈출 할 때까지 재귀적으로 호출하며 진행

def find_start(data, N):        # 시작지점이 항상 최하단은 아님(tc 3번)
    for r in range(N):          # 미로의 크기만큼 반복을 돌면서
        for c in range(N):
            if data[r][c] == 2: # 2(출발점)을 찾아
                return r, c     # 그곳의 좌표를 반환

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    ans = 0
    N = int(input())
    data = [[int(x) for x in input()] for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    sr, sc = find_start(data, N)
    dfs(sr, sc) # 만약 모든 3을 만나지 못하면 ans의 값은 초기값 0인 상태로 반환
    print('#{} {}'.format(tc, ans))
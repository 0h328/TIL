def dfs(k, r, c, val):
    if k == 7:                                             # 7번째 이동이면
        ans.add(val)                                       # set에 추가 & 종료(중복 제거)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]                      # 4방향 이동
        if (0 <= nr < N) and (0 <= nc < N):                # 범위 내에서만 수행
            # k+1 -> 다음 자리, (nr, nc) -> 이동 좌표, val * 10 -> 자릿수 생성
            """
            1. val == 1
             - 1*10 + 1 => 11
            2. val = 11 
             - 11 * 10 + 1 => 111
            ...
            """
            dfs(k+1, nr, nc, val*10+arr[nr][nc])           # 다음 확인 / 새로운 좌표 / 다음 자릿수를 만들기 위한 준비

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = set()                 # 같은 수는 제외 & 방문 했던 곳을 또 가도 되기 때문에 visited 생성하지 않고 진행
    N = len(arr)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for r in range(4):
        for c in range(4):
            dfs(0, r, c, 0)     # 격자판을 돌며 dfs

    print('#{} {}'.format(tc, len(ans)))
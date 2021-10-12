def bfs(r, c):
    global ans
    Q = deque()                     # 노드 => (좌표, 길이, 문자열)
    Q.append((r, c, 1, arr[r][c]))

    while Q:
        r, c, k, num= Q.popleft()
        if k == 7:                  # 7번째 이동
            if num not in result:
                ans += 1
                result[num] = 1
        else:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 4 and 0 <= nc < 4:               # 범위 안에 들어오면
                    Q.append((nr, nc, k+1, num+arr[nr][nc]))  # Q에 추가 & 다음 자리 확인

from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = dict()
    ans = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for r in range(4):
        for c in range(4):
            bfs(r, c)                           # bfs 탐색

    print('#{} {}'.format(tc, len(result)))
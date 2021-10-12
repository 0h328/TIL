import sys
sys.stdin = open('input.txt')


def dfs(idx, x, y, v, s):  # 방향, x좌표, y좌표, 디저트 종류(집합), 각 방향마다의 디저트 수(리스트)
    global res
    if idx == 4:  # base case(모든 방향을 다 돈 경우)
        if x == r and y == c and len(v) > 3:  # 처음 위치이고, 디저트가 4개 이상인 경우(4개 미만이면 사각형 아님)
            res = max(res, len(v))
        return

    dx, dy = dxy[idx]
    if (-1 < x + dx < N) and (-1 < y + dy < N):
        if A[x + dx][y + dy] not in v:
            v.add(A[x + dx][y + dy])
            s[idx] += 1
            dfs(idx, x + dx, y + dy, v, s)  # 백트리킹
            s[idx] -= 1
            v.remove(A[x + dx][y + dy])
    if s[idx]:  # 해당 방향에서 디저트를 얻은 경우
        dfs(idx + 1, x, y, v, s)


ans = []
dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  # 좌상, 우상, 우하, 좌하
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N * N):  # 모든 좌표에서 시작(사실 꼭지점은 필요 없긴함)
        r, c = divmod(i, N)
        dfs(0, r, c, set(), [0, 0, 0, 0])

    res = -1 if res == 0 else res  # 갱신 안됐다면 -1로 지정
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')

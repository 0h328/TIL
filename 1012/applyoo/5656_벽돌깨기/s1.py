import sys
sys.stdin = open('input.txt')

from collections import deque


def down(arr, v):  # 값들을 정렬시키는(내리는) 함수
    for c in v:  # 입력받은 열들만 반복
        t, flag = 0, False
        for r in range(H-1, -1, -1):
            if not arr[r][c]:  # 0인 경우
                t += 1
                flag = True
            if flag and arr[r][c]:  # 0이 이미 나왔고, 0이 아닌 수가 나온 경우
                arr[r+t][c] = arr[r][c]  # t만큼 밀어주기
                arr[r][c] = 0


def bfs(arr, r, c):  # 폭탄을 터트리는 함수
    q = deque([(r, c)])
    v = set()

    while q:
        x, y = q.popleft()

        t = arr[x][y]
        arr[x][y] = 0
        for dx, dy in dxy:  # 상하좌우 반복
            for i in range(1, t):  # 해당 블록의 길이 반복
                nx, ny = x + dx*i, y + dy*i
                if (-1<nx<H) and (-1<ny<W) and arr[nx][ny]:  # 범위내이고 방문한 적 없는 경우
                    q.append((nx, ny))

        v.add(y)  # 방문한 열 추가
    down(arr, v)  # 정렬 실행



def dfs(arr, idx):
    global res
    if idx == N:  # base case
        res = min(res, len([i for i in range(H) for j in range(W) if arr[i][j]]))
        return

    con = 0  # 모두 0인 열 카운트
    for j in range(W):
        arr_copy = [row[:] for row in arr]  # 깊은 복사(deepcopy보다 빠름)
        for i in range(H):  # 맨 위의 열 찾기
            if arr_copy[i][j]: break
        else:  # 해당 열이 모두 0인 경우
            con += 1
            continue
        bfs(arr_copy, i, j)  # 블록 터트리기
        dfs(arr_copy, idx+1)  # 다음 진행

    if con == W: res = 0  # 모든 열이 0인 경우 결과 0으로 갱신


ans = []
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    res = W * H
    dfs(A, 0)
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')

import sys

sys.stdin = open('input.txt')


def dfs(d, nr, nc):
    stack = []
    while True:
        nr, nc = nr + dr[d], nc + dc[d]
        if arr[nr][nc] == 9:
            return stack, 1
        elif arr[nr][nc] == 0:
            arr[nr][nc] = 2
            stack.append((nr, nc))
        else:
            while stack:
                nr, nc = stack.pop()
                arr[nr][nc] = 0
            return stack, 0


# 체크했던 거 되돌리기
def dfs_Back(stack):
    for r, c in stack:
        arr[r][c] = 0


def Connect(idx, temp_res, temp_connected):
    global min_res, connected, unconnected, temp_unconnected

    if temp_unconnected > unconnected:  # POINT) 백트래킹
        return
    if idx == len(cores):
        if temp_connected > connected:  # POINT) 연결된 코어 개수가 늘어나면 무조건 min_res, unconnected도 같이 바뀜
            connected = temp_connected
            min_res = temp_res
            unconnected = temp_unconnected
        elif temp_connected == connected:  # POINT) 연결된 코어 개수가 같은 경우 길이만 교체
            if temp_res < min_res:
                min_res = temp_res
        return

    r, c, directions = cores[idx]
    for d in range(4):  # POINT) 매번 모든 방향을 다 봐줘야 함(연결되지 않더라도 최선일 수 있기 때문)
        length = directions[d]

        if not visited[idx][d]:
            stack, cnt = dfs(d, r, c)
            if cnt == 0:  # POINT) 연결되지 않았을 때 위에서 더할 길이는 0으로, 연결되지 않은 코어수 +1
                length = 0
                temp_unconnected += 1
            visited[idx][d] = 1

            Connect(idx + 1, temp_res + length, temp_connected + cnt)

            visited[idx][d] = 0
            if cnt == 0:
                temp_unconnected -= 1
            else:
                dfs_Back(stack)


T = int(input())

# 0: 전선흐르지 않는 공간, 1 : 전기 연결되지 않은 코어, 2 : 전선, 9: 전기
for t in range(1, T + 1):
    N = int(input())  # N: 가로세로 길이
    arr = [[9] * (N + 2)] + [[9] + list(map(int, input().split())) + [9] for _ in range(N)] + [
        [9] * (N + 2)]  # arr: 전기로 쌓여진 판 (9: 전기)
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    cores = []
    min_res = N * N  # 최소 연결 전선 칸
    connected = 0  # 전기 연결된 코어 개수
    unconnected = 0  # 전기가 연결되지 않은 코어 개수
    temp_unconnected = 0  # POINT) 백트래킹

    # 전기 연결할 코어 좌표(행, 열) 리스트로 만들기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 1:
                # 전기와 붙어있으면 리스트에 좌표 추가하지 않음
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]
                    if arr[nr][nc] == 9:
                        connected += 1
                        break
                else:  # 전기와 연결되지 않은 경우 리스트에 좌표(행, 열) 추가
                    cores.append((i, j, (N - j, N - i, j - 1, i - 1)))  # 우하좌상
                    unconnected += 1  # POINT) 처음 시작할 때 연결되지 않은 코어 수 = 연결해야할 코어수

    visited = [[0, 0, 0, 0] for _ in range(len(cores))]
    Connect(0, 0, connected)

    print('#{} {}'.format(t, min_res))

    # print('cores:', len(cores) + connected, end=' -> ')
    # print(unconnected)
    # print(arr)
    # print(cores)

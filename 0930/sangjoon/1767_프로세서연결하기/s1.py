# 전선의 방향에 대해서 연결가능한지 판별하는 함수입니다.
def check(d1, d2, f1, is_col=True):
    moves = []
    if is_col:
        for i in range(d1, d2):
            if gh[i][f1]:
                return []
            moves.append((i, f1))
    else:
        for i in range(d1, d2):
            if gh[f1][i]:
                return []
            moves.append((f1, i))
    return moves  # 생성될 전선에 대한 정보를 반환합니다.

# 전선을 생성하고 삭제하는 함수입니다.


def connect(moves, con):
    for mx, my in moves:
        gh[mx][my] = con


# 전선으로 연결한 코어들에 대해 dfs 탐색을 수행합니다.
def dfs(idx, cnt, length):

    # 종료조건: 최대 코어개수의 최소 전선길이를 업데이트합니다.
    if idx >= len(boards):
        if cnt > ans[0]:
            ans[0] = cnt
            ans[1] = length
        elif cnt == ans[0]:
            ans[1] = min(ans[1], length)
        return

    # 현재 판별한 코어의 위치를 설정합니다.
    x, y = boards[idx]

    # 코어 위치기준, 상하좌우의 방향으로 탐색합니다.
    directions = [(0, x, y, 1), (x+1, n, y, 1), (0, y, x, 0), (y+1, n, x, 0)]
    for d1, d2, f1, direction in directions:
        moves = check(d1, d2, f1, direction)

        # 이동가능하다면, 전선의 위치를 저장하고 dfs 탐색을 수행합니다.
        if moves:
            connect(moves, 1)
            dfs(idx+1, cnt+1, length + len(moves))
            connect(moves, 0)

    # 현재 코어를 연결하지 않는 경우도 탐색합니다.
    dfs(idx+1, cnt, length)


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    gh, boards = [], []

    # 좌표 및 시작점을 초기화합니다.
    for i in range(n):
        line = list(map(int, input().split()))
        gh.append(line)
        for j in range(1, n-1):
            if 0 < i < n-1 and line[j]:
                boards.append((i, j))

    ans = [0, 0]
    dfs(0, 0, 0)

    print("#{} {}".format(test, ans[1]))

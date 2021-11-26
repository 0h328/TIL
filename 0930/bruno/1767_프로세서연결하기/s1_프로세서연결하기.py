import sys
sys.stdin = open('input.txt')


def count_block(i, j):      # 4방향중 몇방향이 막혀있나?
    global cnt
    if 1 in exi[i][:j]:     # 코어 왼쪽에 1 있나?
        cnt += 1
    if 1 in exi[i][j+1:]:   # 코어 오른쪽에 1 있나?
        cnt += 1
    for m in range(i):      # 코어 위쪽에 1 있나?
        if exi[m][j] == 1:
            cnt += 1
            break
    for n in range(i+1, N): # 코어 아래쪽에 1 있나?
        if exi[n][j] == 1:
            cnt += 1
            break
    return cnt

di = [1, 0, -1, 0]  # 시계방향 / 우하좌상
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    exi = [list(map(int, input().split())) for _ in range(N)]
    # print(exi)
    core_start = []
    block = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if exi[i][j]:
                core_start.append((i, j))
    print(core_start)
    # [(1, 2), (2, 5), (4, 1), (4, 3), (5, 1)]
    # 내부의 코어출발점 -> 4방향 중 막힌 곳이 가장 많은 코어부터 시작
    for s in core_start:
        cnt = 0
        i, j = s
        block.append(count_block(i, j))

    # print(list(enumerate(block)))   # (코어 번호, 막힌 방향수)
    line_order = sorted(list(enumerate(block)), key=lambda x:x[1], reverse=True)        # 주변이 많이 막힌 코어 순으로 정렬
    print(line_order)

    for x in line_order:
        idx = x[0]

    visited = [[0]*N for _ in range(N)]


    # 가장자리까지 도달 가능하다면 그 중 가장 짧은 거리 채택

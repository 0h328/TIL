import sys
sys.stdin = open('input.txt')

from collections import deque
from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def change_data(visit_data, before):
    after = deepcopy(before)
    for r, c in visit_data:
        after[r][c] = 0
        idx = r - 1
        while idx >= 0:
            if after[idx][c] != 0:
                after[r][c], after[idx][c] = after[idx][c], after[r][c]
                r = idx
            else:
                break
            idx -= 1
    return after


def explode(before, row, column):
    global visit_pos, visited
    q = deque()
    q.append((row, column))
    while q:
        r, c = q.popleft()
        visited[r][c] = 1
        visit_pos.add((r, c))

        if before[r][c] <= 1:
            continue
        else:
            for k in range(4):
                for power in range(1, before[r][c]):
                    next_r = r + (dr[k] * power)
                    next_c = c + (dc[k] * power)
                    if 0 <= next_r < H and 0 <= next_c < W and visited[next_r][next_c] == 0 and before[next_r][next_c] != 0:
                        q.append((next_r, next_c))

    sort_visited = sorted(list(visit_pos), key=lambda x: (x[0], x[1]))
    after = change_data(sort_visited, before)
    return after, len(visit_pos)


def find_not_empty(empty_data, column):
    res = H
    for i in range(H):
        if empty_data[i][column]:
            res = i
            break
    return res

def try_position(tr, cur_data, cnt):
    global answer, visit_pos, visited
    visit_pos = set()
    visited = [[0] * W for _ in range(H)]
    if cnt == total:
        answer = total
        return

    if tr == N:
        if answer < cnt:
            answer = cnt
        return

    for i in range(W):
        if find_not_empty(cur_data, i) < H:
            new = explode(cur_data, find_not_empty(cur_data, i), i)
            try_position(tr + 1, new[0], cnt + new[1])
    return

T = int(input())

for case in range(T):
    N, W, H = map(int, input().split())
    ball = [list(map(int, input().split())) for _ in range(H)]
    answer = 0
    total = 0
    for i in range(H):
        for j in range(W):
            if ball[i][j] != 0:
                total += 1
    try_position(0, ball, 0)

    res = total - answer

    print('#{} {}'.format(case + 1, res))
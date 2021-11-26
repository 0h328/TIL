import sys
sys.stdin = open('input.txt')
from collections import deque

def check_dir(x, y):
    d_visit = []
    if x == 0 or x == n-1 or y == 0 or y == n-1:
        return [[set(), 0]]
    for i in range(4):
        new_s = set()
        c = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while -1 < nx < n and -1 < ny < n:
            if (nx, ny) in cores:
                new_s.clear()
                break
            else:
                new_s.add((nx, ny))
                c += 1
            nx += dx[i]
            ny += dy[i]
        if new_s:
            d_visit.append([new_s, c])
    return d_visit


t = int(input())
dx = [0, 0, 1, -1] # 우, 좌, 하, 상
dy = [1, -1, 0, 0]
for idx in range(1, t+1):
    n = int(input())
    cores = []
    res = n * n
    max_connected = 0
    for i in range(n):
        sub = list(map(int, input().split()))
        for j in range(n):
            if sub[j]:
                cores.append((i, j))

    num_core = len(cores)
    cores_visit = []
    for i, j in cores:
        cores_visit.append(check_dir(i, j))# visit집합, visit수, 진행가능여부

    q = deque([(0, set(cores), 0, 0)])# core번호, visited, visitcount, 연결된 core수
    while q:
        core_idx, visited, cnt, connected_core = q.popleft()
        if core_idx == num_core:
            if max_connected < connected_core:
                max_connected = connected_core
                res = cnt
            elif max_connected == connected_core and cnt < res:
                res = cnt
        else:
            for new_visit, new_count in cores_visit[core_idx]:
                if not (new_visit & visited):
                    q.append((core_idx + 1, visited | new_visit, cnt + new_count, connected_core + 1))
            q.append((core_idx + 1, visited, cnt,  connected_core))

    print('#{} {}'.format(idx, res))


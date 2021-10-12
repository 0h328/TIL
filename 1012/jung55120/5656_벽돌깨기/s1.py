import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        check = queue.pop(0)
        for i in range(4):
            pass

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split()) # 구슬의 횟수, W * H 배열
    quest = [list(map(int, input().split())) for _ in range(H)]
    step = 0
    for i in range(N):
        while quest[i][step] > 0:
            bfs(i, step)

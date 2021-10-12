import sys
sys.stdin = open('input.txt')

from collections import deque
from itertools import product
import copy

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs():
    global q, temp

    while q:
        power, i, j = q.popleft()
        for pw in range(1, power):
            for k in range(4):
                ni = i + (di[k] * pw)
                nj = j + (dj[k] * pw)
                if 0 <= ni < H and 0 <= nj < W and temp[ni][nj] != 0:
                    q.append((temp[ni][nj], ni, nj))
                    temp[ni][nj] = 0
        return


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    pro = list(product(range(W), repeat=N))

    for p in pro:
        temp = copy.deepcopy(arr)
        for idx in p:
            q = deque()
            for i in range(H):
                if temp[i][idx] != 0:
                    power = temp[i][idx]
                    q.append((power, i, idx))
                    temp[i][idx] = 0
                    bfs()

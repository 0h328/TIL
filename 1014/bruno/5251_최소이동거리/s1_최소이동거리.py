import sys
sys.stdin = open('input.txt')

for T in range(1, int(input())+1):
    N, E = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(E)]
    node = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for idx in range(E):
        node[road[idx][0]].append((road[idx][1], road[idx][2]))

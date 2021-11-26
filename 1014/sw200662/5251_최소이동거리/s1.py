import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    for i in range(E):
        s, e, w = map(int, input().split())

    G = [[987654321 for _ in range(V + 1)] for _ in range(V + 1)] 
    dist = [987654321] * (V + 1)
    dist[0] = 0
    visited = [0] * (V + 1)

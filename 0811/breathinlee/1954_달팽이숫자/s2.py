import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    moving = [N, N-1, N-1, N-2, N-2, ... , 1, 1]

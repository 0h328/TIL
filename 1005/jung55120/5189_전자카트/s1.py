import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

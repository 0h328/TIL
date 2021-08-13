import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    box = [[0] * 10 for _ in range(10)]

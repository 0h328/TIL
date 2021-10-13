import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cafe_list = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    for a in range(N):
        for b in range(N):
            start_x, start_y = a, b
            cafe(a, b, 0, 0)
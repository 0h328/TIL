import sys
sys.stdin = open("input.txt")


T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

x_direction = [-1, 1, 0, 0]    # 상하좌우
y_direction = [0, 0, -1, 1]    # 상하좌우

action = 0  # 방향
x, y = -1, 0 # 시작 위치
idx = 0





import sys
sys.stdin = open('input.txt')

num = int(input())
num_list = [list(map(int, input().split())) for _ in range(num)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

i, j = 1, 1

for idx in range(4):
    r = i + dr[idx]
    c = j + dc[idx]
    print(num_list[r][c])
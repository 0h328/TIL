import sys
sys.stdin = open('input.txt')

T = int(input())
my_list = [list(map(int, input().split())) for tc in range(T)]

i = 1
j = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for k in range(4):
    nr = i + dr[k]
    nc = i + dc[k]

    print(my_list[nr][nc])
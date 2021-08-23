import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
my_list = [list(map(int, input().split())) for i in range(N)]
# print(my_list)


for i in range(len(di)):
    x, y = 1, 1
    point = my_list[x+di[i]][y+dj[i]]
    print(point)
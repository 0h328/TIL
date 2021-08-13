import sys
sys.stdin = open('input2.txt')

T = int(input())

for Case in range(T):
    N = int(input())
    data_list = [list(map(int,input().split())) for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    total = 0
    for x in range(len(data_list)):
        for y in range(len(data_list[x])):
           for k in range(4):
               new_dx = x + dx[k]
               new_dy = y + dy[k]
               if 0 <= new_dx < N and 0 <= new_dy < N:
                   total += abs(data_list[x][y] - data_list[new_dx][new_dy])

    print('#{} {}'.format(Case+1, total))
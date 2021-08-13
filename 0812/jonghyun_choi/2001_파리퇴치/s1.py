import sys
sys.stdin = open('input.txt')

def catch(map_data,x,y,M):
    x_range = list(range(x,x+M))
    y_range = list(range(y,y+M))
    total = 0
    for r in x_range:
        for c in y_range:
            total += map_data[r][c]
    return total

T = int(input())

for case in range(T):
    N, M = map(int,input().split())
    data_list = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            if catch(data_list,r,c,M) > res:
                res = catch(data_list,r,c,M)
    print('#{} {}'.format(case+1, res))

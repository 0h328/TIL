import sys
sys.stdin = open('input.txt')

def allow_direction(x,y):
    if not(0 <= x < 100 and 0 <= y < 100):
        return False
    return True

def to_left(x,y):
    return x,y-1

def to_right(x,y):
    return x,y+1

def find_index(m,start):
    x, y = 99, start
    while x > 0:
        if allow_direction(to_left(x,y)[0],to_left(x,y)[1]) and m[to_left(x,y)[0]][to_left(x,y)[1]] == 1:
            while allow_direction(to_left(x,y)[0],to_left(x,y)[1]) and m[to_left(x,y)[0]][to_left(x,y)[1]] == 1:
                m[x][y] = 0
                x, y = to_left(x,y)
        elif allow_direction(to_right(x,y)[0],to_right(x,y)[1]) and m[to_right(x,y)[0]][to_right(x,y)[1]] == 1:
            while allow_direction(to_right(x,y)[0],to_right(x,y)[1]) and m[to_right(x,y)[0]][to_right(x,y)[1]] == 1:
                m[x][y] = 0
                x, y = to_right(x,y)
        else:
            m[x][y] = 0
            x -= 1
    return y


for _ in range(10):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(100)]

    start_point = 0
    for p in range(100):
        if map_list[99][p] == 2:
            start_point = p

    print('#{} {}'.format(N,find_index(map_list,start_point)))

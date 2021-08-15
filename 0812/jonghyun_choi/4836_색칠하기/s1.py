import sys
sys.stdin = open('input.txt')

T = int(input())

def point(data):
    res_list = []
    for i in range(data[0],data[2]+1):
        for j in range(data[1],data[3]+1):
            res_list.append([i,j])
    return res_list

for Case in range(T):
    N = int(input())
    data_list = [list(map(int,input().split())) for _ in range(N)]
    # print(data_list)
    red_part = []
    blue_part = []
    for i in data_list:
        if i[-1]==1:
            red_part.append(i[:-1])
        else:
            blue_part.append(i[:-1])
    # print(red_part)
    # print(blue_part)
    red_point = []
    blue_point = []
    for red in red_part:
        red_point += point(red)

    for blue in blue_part:
        blue_point += point(blue)

    # print(red_point)
    # print(blue_point)

    cnt = 0
    for rep in blue_point:
        if rep in red_point:
            cnt += 1

    print('#{} {}'.format(Case+1,cnt))




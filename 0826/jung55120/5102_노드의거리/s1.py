import sys
sys.stdin = open('input.txt')

def find_node(start, end):
    global result
    if check_list[start][end] == 1:
        return result

    for i in range(len(check_list[start])):  # 만약 x, y좌표가 3이면 result = 1
        if check_list[start][i] == 1:
            will_visit.append(i)
            result += 1

    for i in range(len(will_visit)):
        find_node(will_visit[i], end)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    my_num = [list(map(int, input().split())) for i in range(E)]
    check_list = [[0] * (V+1) for i in range(V+1)]
    S, G = map(int, input().split())
    result = 0
    will_visit = []

    # print(my_num)
    # print(check_list)
    # print(V, E)
    # print(S, G)

    for i in range(len(my_num)):          # 왜냐면 방향성이 없으니까 양방향으로 check 가능 !
        x, y = my_num[i][0], my_num[i][1]
        check_list[x][y] = 1
        check_list[y][x] = 1
    print(check_list)
    # check_list[]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    print(find_node(S, G))

    # [[0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 1, 1, 0, 0],
    #  [0, 0, 0, 1, 0, 1, 0],
    #  [0, 1, 1, 0, 0, 0, 0],
    #  [0, 1, 0, 0, 0, 0, 1],
    #  [0, 0, 1, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 1, 0, 0]]





import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    number = 0
    start_x = 0
    start_y = -1
    change_N = N
    move_index = 0
    while change_N > 0:
        num_list = []
        repeat = 0
        if change_N == N:
            while len(num_list) < change_N:
                number += 1
                arr[start_x + dr[move_index]][start_y + dc[move_index]] = number
                num_list.append(number)
                start_x += dr[move_index]
                start_y += dc[move_index]

        else:
            while repeat < 2:
                num_list = []
                while len(num_list) < change_N:
                    number += 1
                    arr[start_x + dr[move_index]][start_y + dc[move_index]] = number
                    num_list.append(number)
                    start_x += dr[move_index]
                    start_y += dc[move_index]
                if repeat < 1:
                    if move_index == 3:
                        move_index = 0
                    else:
                        move_index += 1
                repeat += 1
        if move_index == 3:
            move_index = 0
        else:
            move_index += 1
        change_N -= 1




    print('#{}'.format(N))
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            print(arr[r][c], end=' ')
        print()




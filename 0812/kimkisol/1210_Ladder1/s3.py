import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Ladder(ladder_list):

    #좌우하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    for idx in range(100):
        #출발지점인 경우
        if ladder_list[0][idx] == 1:
            X = idx
            row = 1
            col = idx
            direction = 0
            while row < 98:
                if direction == 0: #아래로 내려가는 방향(좌우 먼저, 이후 아래 탐색)
                    for d in [0, 1, 2]:
                        del_row = row + dr[d]
                        del_col = col + dc[d]
                        if 0 <= del_row < 100 and 0 <= del_col < 100 and ladder_list[del_row][del_col] == 1:
                            row = del_row
                            col = del_col
                            if d == 0: #좌
                                direction = 1
                            elif d == 1: #우
                                direction = 2
                            break
                elif direction == 1: #왼쪽으로 가는 방향(아래먼저, 이후 왼쪽 탐색)
                    for d in [2, 0]:
                        del_row = row + dr[d]
                        del_col = col + dc[d]
                        if 0 <= del_row < 100 and 0 <= del_col < 100 and ladder_list[del_row][del_col] == 1:
                            row = del_row
                            col = del_col
                            if d == 2:
                                direction = 0
                            break
                elif direction == 2: #오른쪽으로 가는 방향(아래먼저, 이후 오른쪽 탐색)
                    for d in [2, 1]:
                        del_row = row + dr[d]
                        del_col = col + dc[d]
                        if 0 <= del_row < 100 and 0 <= del_col < 100 and ladder_list[del_row][del_col] == 1:
                            row = del_row
                            col = del_col
                            if d == 2:
                                direction = 0
                            break
            if ladder_list[row + 1][col] == 2:
                return X
    return False

for t in range(1, 11):
    input()
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(t, Ladder(ladder_list)))
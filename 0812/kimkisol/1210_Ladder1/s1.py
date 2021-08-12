import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Ladder(ladder_list):
    #좌우하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    for idx in range(1, 101):
        #출발지점인 경우
        if ladder_list[0][idx] == 1:
            row = 1
            col = idx
            direction = 2
            while row < 98:
                #방향에 따른 탐색 순서 설정
                if direction == 0: #왼쪽으로 가는 방향(아래먼저, 이후 왼쪽 탐색)
                    direction_idx = [2, 0]
                elif direction == 1: #오른쪽으로 가는 방향(아래먼저, 이후 왼쪽 탐색)
                    direction_idx = [2, 1]
                elif direction == 2:  # 아래로 내려가는 방향(좌우 먼저, 이후 아래 탐색)
                    direction_idx = [0, 1, 2]
                #direction 방향에 맞춰 탐색후 1이 보이면 이동
                for d in direction_idx:
                    del_row = row + dr[d]
                    del_col = col + dc[d]
                    if ladder_list[del_row][del_col] == 1:
                        row = del_row
                        col = del_col
                        direction = d
                        break
        #도착지가 2이면 idx - 1 return
        if ladder_list[row + 1][col] == 2:
            return idx - 1 #테두리 설정해줬기 때문에 1 빼줌
    return False

for t in range(1, 11):
    input()
    #idx 에러 안 나도록 테두리 설정
    ladder_list = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    print('#{} {}'.format(t, Ladder(ladder_list)))
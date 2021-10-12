import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_room(x, y, cnt):
    global ans,ans_num
    if cnt > ans:
        ans = cnt
        ans_num = room_list[a][b]
    if cnt == ans and ans_num > room_list[a][b]:
        ans = cnt
        ans_num = room_list[a][b]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < N and new_y < N and room_list[new_x][new_y] == room_list[x][y] + 1:
            find_room(new_x, new_y, cnt + 1)



for tc in range(1, T + 1):
    N = int(input())
    room_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    ans_num = 100000
    for a in range(N):
        for b in range(N):
            find_room(a, b, 1)
    print('#{} {} {}'.format(tc,ans_num,ans))
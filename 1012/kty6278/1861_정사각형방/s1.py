import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(row, col):
    global result, room_num, cnt
    cnt = 1
    que = deque()
    que.append([row, col])
    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]
            if 0 <= nrow < n and 0 <= ncol < n:
                if room_list[nrow][ncol] == room_list[row][col] + 1:
                    que.append([nrow, ncol])
                    cnt += 1

    if cnt > result:
        result = cnt
        room_num = room_list[row][col] - result + 1
    elif cnt == result:
        if room_num > room_list[row][col] - result + 1:
            room_num = room_list[row][col] - result + 1


for tc in range(int(input())):
    n = int(input())
    room_list = [list(map(int, input().split())) for _ in range(n)]
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    result = 0                                    # 최종 지나온 방 개수
    cnt = 0                                       # 누적으로 세는 현재 방 개수
    room_num = n**2                               # 방 번호
    result_list = []                              # 방 번호랑 방 개수 넣을 리스트

    for i in range(n):
        for j in range(n):
            bfs(i, j)
    result_list.append((room_num, result))
    print('#{}'.format(tc+1), end = ' ')
    print(*result_list[0])
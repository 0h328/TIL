# 반복문 돌리기가 훨씬 낫다는 지윤이의 조언(dfs는 시간초과 날 것이라는데...? 글고 어떻게 계산하지? 흠.. :(
# 해결이 되었다 !!!! 행복 ^_________^

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global result, room_number
    if cnt > result:                 # cnt의 수가 result 값보다 크면
        room_number = room[x][y]     # room_number에 정사각형방의 번호를 저장
        result = cnt                 # result에는 cnt값을 저장

    elif cnt == result:              # 만약 result와 cnt가 같은데 room_number의 수가 더 크면
        if room_number > room[x][y]:
            room_number = room[x][y] # 작은 수를 저장


    for i in range(4):               # 4방향 돌면서 확인
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[x][y] - 1: # 정사각형방 안에 있고, 1만 차이날 때
            dfs(nx, ny, cnt+1)       # 재귀쓰 사용
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    result = 1
    room_number = 1000000
    for i in range(N):
        for j in range(N):
            dfs(i, j, 1)    # 리스트의 좌표와 cnt 가지고 다니기
    print('#{} {} {}'.format(tc, room_number, result))
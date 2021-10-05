'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고,
각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때,
지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면
이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
'''


def DFS_SUM(start):
    global sum_num
    global min_num
    x, y = start

    if x == N-1 and y == N-1:           # 마지막 칸에 도달 하면!
        if min_num > sum_num:           # 작으면 그게 최소
            min_num = sum_num

    for i in range(2):      # 우, 하만 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:        # 범위
        # if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:        # 범위, 방문여부
            if sum_num > min_num:               # 가지치기, 이미 넘었으면 할 이유가 없음
                return

            # visited[nx][ny] = 1         # 방문 처리
            sum_num += number[nx][ny]   # 숫자 더해줌
            DFS_SUM((nx, ny))           # 재귀
            # visited[nx][ny] = 0         # 방문 취소
            sum_num -= number[nx][ny]   # 숫자 빼줌


import sys
sys.stdin = open('input.txt')

dx = (0, 1)     # 우, 하
dy = (1, 0)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    # print(number)
    # visited = [[0] * N for _ in range(N)]
    sum_num = number[0][0]                              # 시작 지점 먼저 넣고 시작
    min_num = 987654321                                 # 최소 비교를 위해서 설정

    DFS_SUM((0, 0))                                     # 시작은 (0, 0)

    print('#{} {}'.format(tc, min_num))


#1 15
#2 18
#3 33
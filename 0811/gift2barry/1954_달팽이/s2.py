import sys
sys.stdin = open('input.txt')

# thought process: 16분
# 2차원 배열에서 벽을 만날 때 마다 방향전환
# N * N 만큼의 숫자를 모두 입력할 때까지 반복


# 막판에 륜기님 도움받고 2시간만에 품..
for tc in range(1, int(input())+1):

    N = int(input())

    table = [[0]*N for _ in range(N)]   # 2차원 배열 생성

    x, y = 0, 0         # 좌표값 초기화
    table[x][y] = 1     # 시작지점에 첫번째 숫자 입력

    for idx in range(2, N*N+1):

        # 각각 인덱스 범위를 벗어나지 않고 다음 좌표가 0 일때
        if y+1 < N and table[x][y+1] == 0:                # 우측이동시
            y += 1
        elif x+1 < N and table[x+1][y] == 0:              # 아래이동시
            x += 1
        elif y-1 >= 0 and table[x][y-1] == 0:              # 좌측이동시
            y -= 1
        elif x-1 >= 0 and table[x-1][y] == 0:              # 위쪽이동시
            x -= 1

        table[x][y] = idx

    print('#{}'.format(tc))
    for i in range(N):
        print(*table[i])












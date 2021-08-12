import sys
sys.stdin = open('input.txt')

test_case = int(input())

dy = [0, 1, 0, -1]                  # 진행 방향이 오른쪽 -> 아래 -> 왼쪽 -> 위
dx = [1, 0, -1, 0]


for tc in range(1, test_case+1):
    num = int(input())
    answer = [[0]*num for _ in range(num)]
    direction = 0                   # 초기 진행 방향 오른쪽
    x, y = 0, 0                     # 달팽이 초기 위치

    val = 1
    while val <= num**2:            # 리스트에 입력할 숫자
        answer[y][x] = val          # 리스트에 먼저 값 지정
        val += 1                    # 다음 값

        x += dx[direction]          # 다음 인덱스
        y += dy[direction]

        if x < 0 or y < 0 or x >= num or y >= num or answer[y][x] != 0:     # 다음 인덱스가 범위를 벗어나거나 이미 지나친 경우
            x -= dx[direction]      # 뒤로 다시 돌아감
            y -= dy[direction]

            direction = (direction+1) % 4   # 방향전환

            x += dx[direction]      # 다음 인덱스
            y += dy[direction]


    print('#{}'.format(tc))

    for i in range(num):
        print(*answer[i])
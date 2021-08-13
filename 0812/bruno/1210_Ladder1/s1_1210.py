import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for idx in range(len(ladder[99])):      # 도착점의 인덱스 찾기
        if ladder[99][idx] == 2:            # 사다리 마지막 행 탐색
            arrive_j = idx                  # 값이 2인 곳의 idx 반환

    i = 99
    j = arrive_j
    button = 1

    while button:

        i, j = i + dr[4], j + dc[4]             # 일단 위로 이동

        if ladder[i][j - 1]:                    # 왼쪽에서 1을 만나면
            while ladder[i][j - 1]:
                i, j = i + dr[3], j + dc[3]     # 좌측으로 이동

        elif ladder[i][j + 1]:                  # 오른쪽에서 1을 만나면
            while ladder[i][j + 1]:
                i, j = i + dr[1], j + dc[1]     # 우측으로 이동
        
        if i == 0:                              # 맨 윗행에 도착하면
            start_point = j                     # 열 값 반환
            button = 0                          # 반복문 종료

    print('#{} {}'.format(tc, start_point))



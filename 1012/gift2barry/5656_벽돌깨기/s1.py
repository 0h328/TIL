'''
미 해결
총 소요시간 : 1시간 26분
thought process: 28분 20초
2 ≤ W ≤ 12  => column
2 ≤ H ≤ 15  => row

전체 frame:
매번 쏠 때 마다, 숫자의 총 합이 가장 큰 컬럼을 타겟. (조건: 주어진 공 개수 안에, 1이 아닌 숫자에 도달 가능할 때)
매번 쏘고 나서, 이동 원소 확인
모든 공 소진하면, 리스트 돌면서 남은 블럭 개수 반환

탐색법:
방향델타값 활용 (상 우 하 좌).
공이 맞춘 블럭의 숫자만큼 방향델타값 길이 조정

1. 컬럼마다 원소 총 합 계산 후 리스트에 입력
2. 가장 높은 값 컬럼부터 주어진 공 개수 안에, 1이 아닌 숫자에 도달 가능한지 확인
3. 불가능하면 해당 인덱스 원소 0 으로 바꾸고 2번 반복 (while loop 공 개수 0 될 때 까지)
4. 가능하면 쏘고, bfs활용 (영향받는 벽돌들 queue에 넣고, 영향범위 탐색 함수 활용하여 루프)
5. refresh() 함수로 블럭들이 터진 board를 한번 정리

# visited 사용하지않고 메인 보드를 조작해보자

'''


import sys
sys.stdin = open('input.txt')


def bfs(r, c, block):

    Q = [block]
    while Q:
        v = Q.pop(0)
        # 상 우 하 좌
        dr = [-v, 0, v, 0]
        dc = [0, v, 0, -v]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            for num, idx in enumerate(board[[r][c]:[nr][nc]]):
                if num > 1:
                    Q.append(row, column, block_size)      # 좌표와 블럭을 넣어서 bfs 지속

            '''
                # board[[r][c]:[nr][nc]] 이 범위 안의 모든 블럭들 0으로 변환
                # refresh() 함수로 블럭들이 터진 board를 한번 정리
            '''

input()
for tc in range(1, 2):

    N, W, H = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(H))
    tmp = [0] * W               # 각 컬럼마다의 원소 총합

    for i in range(W):          # tmp 에 column 마다 원소 총합 넣어주기
        nums = 0
        for j in range(H):
            nums += board[j][i]
        tmp[i] = nums
    print(tmp)

    for k in range(W):          # 타깃 확인
        target = max(tmp)
        idx = tmp.index(target)
        if N:
            for i in range(H):
                if board[i][idx] > 1 and board[i-N][idx] == 0:        # 1 이상의 원소를 칠 수 있을때
                    while board[i][idx]:                              # 위에있는 숫자 1들 만큼 공 횟수를 줄이고
                        i -= 1
                    bfs(i, idx, board[i][idx])                        # 파괴할 블록 위치 r & c, 해당 블록 원소 크기
                else:
                    tmp[idx] = 0





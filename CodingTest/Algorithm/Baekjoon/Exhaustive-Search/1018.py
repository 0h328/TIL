import sys
sys.stdin = open('input.txt')

# N: 행, M: 열
N, M = map(int, input().split())

board = []
cnt = 987654321
for _ in range(N):
    chess = input()
    board.append(chess)

for i in range(N-7):                        # 8x8을 조사하기 위한 범위 설정
    for j in range(M-7):
        case1 = 0
        case2 = 0
        for k in range(i, i+8):             # 8개의 행만 조사
            for l in range(j, j+8):         # 8개의 열만 조사
                if (k+l) % 2 == 0:          # 시작점, 2번째점, 4번째점.. (짝수)
                    if board[k][l] == 'B':  # B로 칠해졌으면
                        case1 += 1          # case1을 추가
                    else:                   # W로 칠해졌으면
                        case2 += 1          # case2를 추가
                else:                       # 1번째점, 3번째점, 5번째점.. (홀수)
                    if board[k][l] == 'B':
                        case2 += 1          # 이웃하는 부분이 같은색이면 칠하면 안되니까
                    else:
                        case1 += 1
        if cnt > min(case1, case2):
            cnt = min(case1, case2)

print(cnt)



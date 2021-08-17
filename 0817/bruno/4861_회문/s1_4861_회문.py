import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    square = [list(input()) for _ in range(N)]
    zip_square = list(zip(*square))
    print(zip_square)
    break
    for i in range(N):
        for j in range(N - M + 1):
            # 행 기준 회문 찾기
            for k in range(M // 2):
                if square[i][j + k] != square[i][j + M - 1 - k]:
                    break
            else:
                result_row = ''.join(square[i][j:j+M])
                print('#{} {}'.format(tc, result_row))
            # 열 기준 회문 찾기
            for k in range(M//2):
                if square[j + k][i] != square[j + M - 1 - k][i]:
                    break
            else:
                result_col = ''
                for k in range(M):
                    result_col += square[j + k][i]
                print('#{} {}'.format(tc, result_col))



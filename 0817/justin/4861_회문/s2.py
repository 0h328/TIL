import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    for i in range(N):              # 행
        for j in range(N-M+1):      # N-M+1 => 찾아야하는 회문의 길이
            for k in range(M//2):   # 회문 체크
                if data[i][j+k] != data[i][j+M-k-1]: # 다른 경우 반복 종료 (핵심은 j+M-k-1라는 일반항)
                    break
            else:                                           # 회문인 경우
                print('#{}'.format(tc), end=' ')
                for k in range(j, M+j):
                    print('{}'.format(data[i][k]), end='')  # 행 우선 출력
                print()

    for i in range(N):               # 열
        for j in range(N-M+1):
            for k in range(M // 2):
                if data[j+k][i] != data[j+M-k-1][i]:
                    break
            else:
                print('#{}'.format(tc), end=' ')
                for k in range(j, M+j):
                    print('{}'.format(data[k][i]), end='')
                print()

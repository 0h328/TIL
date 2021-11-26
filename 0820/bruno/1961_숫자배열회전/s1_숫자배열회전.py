import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    original = [list(map(int, input().split())) for _ in range(N)]
    new_90 = [[0 for _ in range(N)] for _ in range(N)]
    # 90도 회전
    for i in range(N):
        for j in range(N):
            new_90[i][j] = original[N-1-j][i]
    new_180 = [[0 for _ in range(N)] for _ in range(N)]
    # 180도 회전
    for i in range(N):
        for j in range(N):
            new_180[i][j] = original[N-1-i][N-1-j]
    new_270 = [[0 for _ in range(N)] for _ in range(N)]
    # 270도 회전
    for i in range(N):
        for j in range(N):
            new_270[i][j] = original[j][N-1-i]
    # 출력
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, new_90[i])), ''.join(map(str, new_180[i])), ''.join(map(str, new_270[i])))
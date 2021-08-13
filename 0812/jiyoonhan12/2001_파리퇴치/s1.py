import sys
sys.stdin = open('input.txt')

T =  int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_group = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            current_group = 0
            for k in range(M):
                for l in range(M):
                    current_group += arr[i+k][j+l]
            if current_group > max_group:
                max_group = current_group

    print('#{} {}'.format(t, max_group))
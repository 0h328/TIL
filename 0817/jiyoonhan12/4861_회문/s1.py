import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    turn_arr = list(zip(*arr))

    for n in range(N):
        for k in range(N):
            temp1 = []
            temp2 = []

            if k + M <= N:
                # 가로
                temp1 = arr[n][k:k + M]
                if list(temp1) == list(reversed(temp1)):
                    print('#{} {}'.format(t, ''.join(temp1)))
                # 세로
                temp2 = turn_arr[n][k:k + M]
                if list(temp2) == list(reversed(temp2)):
                    print('#{} {}'.format(t, ''.join(temp2)))
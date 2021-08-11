import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split()))
    station = [0] * (N+1)
    charge_cnt = 0
    for j in charge_station:
        station[j] = 1

    position = K
    while position < N:
        check = 0

        for m in range(K):
            if station[position - m] == 1:
                check += 1
                position = position -m + K
                break
        if check == 1:
            charge_cnt += 1
        elif check == 0:
            charge_cnt = 0
            break


    print('#{} {}'.format(i, charge_cnt))
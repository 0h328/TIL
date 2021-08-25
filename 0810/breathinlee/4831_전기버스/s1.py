import sys
sys.stdin = open("input.txt")

N = int(input())

for tc in range(1, N+1):
    K, N, M = map(int, input().split())
    bus_charger = list(map(int, input().split()))
    cnt = 0
    for i in range(M-1):
        if bus_charger[i+1] - bus_charger[i] > K:
            break
    else:
        bus_moves = 0
        while bus_moves < N:
            for j in range(M):
                bus_moves += 1
                if bus_moves < K:
                    break
                elif bus_moves in bus_charger:
                    cnt += 1
                    bus_moves += K
                else:
                    bus_moves -= 1
    print('#{} {}'.format(tc, cnt))
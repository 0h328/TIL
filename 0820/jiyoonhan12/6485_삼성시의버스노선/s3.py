import sys
sys.stdin = open('input.txt')

# 2. 정류장을 미리 계산해보자
T = int(input())

for t in range(1, T+1):
    N = int(input())

    start = [0] * 5001
    end = [0] * 5001
    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

    P = int(input())
    print('#{}'.format(t), end=' ')
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()
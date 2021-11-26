import sys
sys.stdin = open('input.txt')

# 3. 정류장을 미리 계산해보자2
T = int(input())

for t in range(1, T+1):
    N = int(input())

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input())
    print('#{}'.format(t), end=' ')
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()
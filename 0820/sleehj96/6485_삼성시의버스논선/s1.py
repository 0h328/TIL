import sys

sys.stdin = open('input.txt')


T = int(input())

tc = 1
while tc <= T:
    bus_stop = [0] * 50001
    ans_list = []
    N = int(input())

    for _ in range(N):
        A, B = map(int, input().split())
        for stop in range(A, B+1):
            bus_stop[stop] += 1

    P = int(input())
    for _ in range(P):
        ans_list.append(bus_stop[int(input())])

    # print(bus_stop)
    # print(*ans_list)
    print('#{}'.format(tc), end=' ')
    print(*ans_list)
    # break
    tc += 1
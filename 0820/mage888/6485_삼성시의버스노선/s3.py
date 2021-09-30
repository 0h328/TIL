import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = []
    for _ in range(N):
        A, B = map(int, input().split())
        bus_stop.append((A, B))

    cnt_list = []

    P = int(input())
    for _ in range(P):
        C = int(input())
        cnt = 0
        for i in range(len(bus_stop)):
            if C in range(bus_stop[i][0], bus_stop[i][1]+1):
                cnt += 1
        cnt_list.append(cnt)

    print('#{} {}'.format(tc, ' '.join(map(str, cnt_list))))





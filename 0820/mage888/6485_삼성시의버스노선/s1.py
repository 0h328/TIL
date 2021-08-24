def bus_count(bus_stop):

    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1

    return cnt


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_route = []
    for _ in range(N):
        A, B = map(int, input().split())
        bus_route.append((A, B))

    P = int(input())
    ans = []    # 버스 수를 저장해 놓을 리스트

    for _ in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))

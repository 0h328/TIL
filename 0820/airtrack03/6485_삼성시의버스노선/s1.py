'''
P개의 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지?
=> 각 정류장에서 이전 정류장에서 계산된 값에 해당 정류장에서 새롭게 출발하는 버스를 더하고 해당 정류장에 도착하는 버스를 빼준다!
=> 잘 이해가 안됨....
'''

import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 버스 노선 개수
    bus_limit = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())    # P 개의 정류장
    bus_stations = [int(input()) for _ in range(P)]

    bus_limit.sort(key=lambda x: (x[0], x[1]))
    ans = [0 for _ in range(P)]

    for i in range(P):
        for bus in bus_limit:
            if bus_stations[i] < bus[0]:
                continue
            elif bus_stations[i] <= bus[1]:
                ans[i] += 1
            else:
                continue
    print('#{} {}'.format(tc, ' '.join(list(map(str, ans)))))

import sys

sys.stdin = open('input.txt')

t = int(input())

i = 1
while i <= t:
    k, n, m = map(int, input().split())
    # bus_stops = [0] * (n + 1)
    gas_stops = list(map(int, input().split()))

    # for gas_stop in gas_stops:
    #     bus_stops[gas_stop] = 1

    rem_gas = k     # 처음 기름 만땅
    ans = 0         # 주유 횟수

    for idx in range(n):    # 모든 정거장을 거침

        if idx in gas_stops:    # 주유소가 있는 정거장

            if idx == gas_stops[-1]:    # 마지막 정거장이면 (IndexError 방지)
                way_to_go = n - idx     # 종착역까지 남은 거리를 계산해보고
                if way_to_go <= rem_gas:    # 지금 기름으로 충분히 갈 수 있으면
                    break                   # 반복문 탈출
                else:                       # 아니면
                    ans += 1                # 주유 횟수 +1
                    # rem_gas = k             # 기름 주유

            else:                       # 마지막 정거장이 아니면
                way_to_go = gas_stops[gas_stops.index(idx) + 1] - idx   # 그 다음 주유소까지 거리

                if rem_gas < way_to_go:     # 지금 기름으로 부족하면
                    ans += 1                # 주유
                    rem_gas = k

        if rem_gas == 0:    # 기름이 없으면
            ans = 0         # ans = 0
            break           # 못 감

        rem_gas -= 1        # 반복문 한번씩 돌 때마다 기름 -1

    print('#{0} {1}'.format(i, ans))
    i += 1

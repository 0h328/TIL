import sys

sys.stdin = open('input.txt')

t = int(input())

i = 1
while i <= t:
    k, n, m = map(int, input().split())
    bus_stops = [0] * (n + 1)
    gas_stops = list(map(int, input().split()))

    for gas_stop in gas_stops:
        bus_stops[gas_stop] = 1

    rem_gas = k
    ans = 0

    for idx in range(n):

        if idx in gas_stops:

            if idx == gas_stops[-1]:
                way_to_go = n - idx
                if way_to_go <= rem_gas:
                    break
                else:
                    ans += 1
                    rem_gas = k

            else:
                way_to_go = gas_stops[gas_stops.index(idx) + 1] - idx

                if rem_gas < way_to_go:
                    ans += 1
                    rem_gas = k

        if rem_gas == 0:
            ans = 0
            break

        rem_gas -= 1

    print('#{0} {1}'.format(i, ans))
    i += 1

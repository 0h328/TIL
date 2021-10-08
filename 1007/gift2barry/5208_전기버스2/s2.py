def find_min_change(n):
    global min_change
    global change
    global nn

    if n >= N:
        if min_change > change:
            min_change = change
        return

    if battery[n] + 1 >= N:
        min_change = 1
        return

    else:
        for i in range(battery[n], nn, -1):
            nn += (n + i)
            change += 1

            if nn < N:
                find_min_change(nn)

            nn -= (n + i)
            change -= 1


import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    station_battery = list(map(int, input().split()))
    # print(station_battery)
    min_change = 987654321
    change = 0
    nn = 0
    N = station_battery[0]
    battery = station_battery[1:]

    find_min_change(0)

    print('#{} {}'.format(tc, min_change))
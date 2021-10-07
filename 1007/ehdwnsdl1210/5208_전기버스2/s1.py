'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다.
정류장에는 교체용 충전지가 있는 교환기가 있고,
충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.

충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
정류장과 충전지에 대한 정보가 주어질 때,
목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오.
단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
'''

def find_min_change(n):
    global min_change
    global change

    for i in range(battery[n], 0, -1):
        change += 1

        if n + i < N - 1:
            if min_change > change:
                find_min_change(n + i)

        else:
            if min_change > change:
                min_change = change

        change -= 1


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    station_battery = list(map(int, input().split()))
    # print(station_battery)
    min_change = 987654321
    change = 0

    N = station_battery[0]
    battery = station_battery[1:]

    find_min_change(0)

    print(f'#{tc} {min_change - 1}')

#1 1
#2 2
#3 5
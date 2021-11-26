"""
목적지에 도착하는 데 필요한 최소한의 교환횟수 출력할 것(출발지에서의 배터리 장착x)
마지막 정류장에는 배터리 없음/출발지 배터리 장착은 카운트x
"""
def check(location):
    global min_charge, charge

    if min_charge < charge:
        return

    if location >= station-1:
        if min_charge >= charge:
            min_charge = charge
            return

    for idx in range(location+battery_capacity[location], location, -1):
        charge += 1
        check(idx)
        charge -= 1


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    charging_info = list(map(int, input().split()))
    station = charging_info[0]       # 정류장 수
    battery_capacity = [0] * station    # 정류장 별 배터리 용량
    for i in range(station-1):
        battery_capacity[i] = charging_info[i+1]
    min_charge = 101
    charge = -1            # 교환횟수

    check(0)     # 현재위치

    print('#{} {}'.format(tc, min_charge))
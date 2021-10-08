def solve(num, remaining_battery, swap_cnt):                 # 정류장 번호, 남은 배터리 용량, 교환 횟수
    global ans
    if num >= bus_stops[0]:                                  # 종점에 온 경우(혹은 넘은 경우)
        # ans = max(ans, swap_cnt)
        if ans > swap_cnt:                                   # (필요한 경우) 최소 교환 횟수 갱신
            ans = swap_cnt
    else:
        if remaining_battery > 0:                            # 아직 배터리가 남았다면
            solve(num+1, remaining_battery-1, swap_cnt)      # 다음 정류장으로, 배터리를 교체하지 않고 1만 감소 시킴, 배터리 교환 횟수는 그대로 유지
        if swap_cnt < ans:                                   # 현재까지의 배터리 교환 횟수가 최소 교환 횟수보다 적으면 (배터리를 교환해도 최소 교환 횟수를 넘지 않을 수 있으니)
            solve(num+1, bus_stops[num]-1, swap_cnt+1)       # 다음 정류장으로, 배터리 교환 o , 교환 횟수를 하나 증가 시키자

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    bus_stops = list(map(int, input().split()))     # 0번째 -> 정류장 수 / 1번째 ~ N-1: 각 정류장 별 충전지
    ans = 987654321
    solve(2, bus_stops[1]-1, 0)                     # 정류장 번호, 남은 배터리 용량(1번 정류장에서 출발하는 걸 가정해서 1 줄이고 시작), 교환 횟수
    print('#{} {}'.format(tc, ans))

"""
1) 2 
 - 1번 정류장에서 2번으로 출발 -> 2를 바로 넘김
 - 출발지에서의 배터리 장착은 교환횟수에서 제외
2) bus_stops[1]-1
 - 1번에서 2번으로 가는 동시에 소모되는 배터리
 - 1번 정류장의 배터리 용량 1 소모 -> bus_stops[1] -1 
3) 0
 - 교환 횟수 cnt
"""
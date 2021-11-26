import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())         # K: 이동할 수 있는 최대 거리 / N: 마지막 종점의 위치 / M: 충전소의 개수
    chargers = list(map(int, input().split()))  # 충전소
    bus_stop = [0] * (N+1)                      # 정류장 -> N번 종점까지 가야 하니까 N+1 크기로 생성
    for i in range(M):                          # 충전소 표시
        bus_stop[chargers[i]] = 1
    bus = 0     # 버스의 위치
    ans = 0     # 충전 횟수

    while True:
        bus += K      # 버스를 최대 이동거리 만큼 이동 시키자
        if bus >= N:  # 버스가 종점에 도착하거나 종점을 지나 더 나아간 경우는 중지
            break
        for i in range(bus, bus-K, -1): # 내 자리 직전(bus-K -> bus-K-1)까지 가보자
            if bus_stop[i]:             # 이동한 곳에 충전기가 있으면
                ans += 1                # 충전 count
                bus = i                 # 버스의 위치를 이동한 곳으로 변경
                break                   # 종료 -> 이후에 갈 수 있는 만큼 또 최대로 이동
        else:           # 충전기를 못찾을 때 (반복문에서 break를 못만난 경우) -> for & else 구문
            ans = 0     # 0으로 변경하고
            break       # 종료
    print('#{} {}'.format(tc, ans))
'''
2중 반복 사용
외부 반복에서의 인덱스는 버스가 출발하는 위치
내부 반복에서 버스 위치 + 1 ~ + charge_move 까지 순환함
제일 먼곳부터 충전소가 있는지 체크하고 있으면 그쪽으로 버스 위치 인덱스 증가
버스 앞에 충전소 없으면 정답으로 0 출력
'''

import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    charge_move, destination, charger = map(int, input().split())   # 충전으로 이동가능한 최대 거리, 목적지까지 거리, 충전소 갯수
    charger_list = list(map(int, input().split()))                  # 충전소 위치가 적힌 리스트
    station_list = [0] * (destination+1)                            # 정류장의 충전소 유뮤 / 0:없음 1:있음
    answer = 0                                                      # 정답을 담을 변수

    for e in charger_list:                                          # 정류장 충전소 유무 설정
        station_list[e] = 1

    bus_idx = 0                                                     # 버스의 현재 위치 인덱스 값
    while bus_idx < destination - charge_move:                      # 버스가 한번에 목적지에 도착가능한 인덱스 범위내에 도달하기 전까지 반복
        for i in range(bus_idx+charge_move, bus_idx, -1):           # 버스가 이동 가능한 먼 거리부터 충전소가 있는지 탐색
            if station_list[i] == 1:                                # 충전소 있으면 버스 현재 위치를 옮김
                bus_idx = i
                answer += 1
                break
        if bus_idx != i:                                            # 버스가 움직일수있는 범위내에 충전소 없다면, 반복문 종료
            answer = 0
            break



    print('#{} {}'.format(tc, answer))
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())             # K => 한번에 이동 가능한 최대 거리 / N => 종점 버스 정류장 / M => 충전소의 개수
    gas_stations = list(map(int, input().split()))  # 충전소
    bus_stations = [i for i in range(N+1)]          # 버스 정류장
    charged_gas_count = 0                           # 충전 횟수
    check_loop_count, original_K = K, K             # loop 횟수 카운트, 변화하는 K 값 대신 원본 값 저장

    while K < N:  # 종점에 도달할 때까지 계속 반복
        if bus_stations[K] in gas_stations and check_loop_count != 0: # 만약 K만큼 이동 했는데 거기에 충전소가 있고 뒤로 돌아 다시 시작점으로 온게 아니라면
            charged_gas_count += 1  # 충전 횟수 카운트
            K += original_K         # K에서 +K만큼 이동
            check_loop_count = original_K # loop 카운트를 다시 K만큼 충전 -> 충전소를 만났다는 말은? 다시 K-1만큼은 뒤로 가도 된다는 의미 -> 다시 초기화
        elif bus_stations[K] not in gas_stations and check_loop_count != 0: # 만약 충전소가 없고 다시 시작점으로 돌아온게 아니라면
            K -= 1                # 뒤로 한 칸 이동하자
            check_loop_count -= 1 # loop 카운트를 하나 감소 -> 이게 뒤로 간다는 것을 의미
        else:
            charged_gas_count = 0 # 이게 아닌 경우 도착을 못하는 경우이므로 0 & 종료
            break
    ans = charged_gas_count
    print('#{} {}'.format(tc, ans))
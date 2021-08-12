import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())                                  # K -> 갈 수 있는 최대 거리 / N -> Station 개수 / M -> 충전소 개수
    chargers = list(map(int, input().split()))                           # 충전소
    stations = [True if n in chargers else False for n in range(N+1)]    # 충전기가 있으면 T, 아니면 F (정류장이 0번부터 시작하니 N+1)
    charge_count = last_charge = 0                                       # 총 충전 횟수 / 마지막 충전한 위치 인덱스 초기화
    current = K                                                          # 시작과 동시에 현 위치 갱신 -> 최대로 일단 갈 수 있을 만큼 가자

    while current < N:              # 종점에 도착하지 않았을 때까지 계속 반복 (같거나 큰 경우가 종점을 도착하거나 그 이상으로 간 경우)
        if last_charge == current:  #3. 한칸씩 뒤로 가다가 마지막 충전 위치에 도착했다면? 한번의 충전으로는 더이상 갈 수 없음을 의미
            charge_count = 0        # 실패
            break
        if stations[current]:         #1. 현 위치에서 충전 가능하다면? (충전기가 있다면)
            last_charge = current     # 마지막 충전위치 갱신
            charge_count += 1         # 충전 횟수 +1
            current += K              # 갈 수 있을 만큼 최대 전진
        else:                   #2. 현 위치 충전 불가능하면
            current -= 1        # 1칸 전으로 (충전소 나올때까지 뒤로가기)

    print('#{} {}'.format(tc, charge_count))
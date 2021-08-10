import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split())) # 충전소 위치 리스트

    position = 0 # 첫 위치
    charge_cnt = 0 # 충전 횟수

    for m in range(M):
        if m != M-1: # 마지막 충전소 아닐 때
            if charger[m] > position + K:
                charge_cnt = 0
                break
            elif charger[m] <= position + K < charger[m + 1]:
                position = charger[m]
                charge_cnt += 1
            else:
                continue

        else:
            if position + K >= N:
                break
            elif charger[m] <= position + K:
                position = charger[m]
                charge_cnt += 1


    print('#{} {}'.format(t, charge_cnt))

    # 0에서 N까지 가는데 정류장은 charger에 정해져 있고
    # 루프 돌 거 (0, 남은정류장개수)
    # 정류장i < 현재위치 + K < 정류장i+1 이면 정류장i로 이동



    # 만약에 현재위치 + K < 현재 가장 가까운 정류장i 면 바로 0 출력
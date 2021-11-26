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
            if charger[m] > position + K: # 충전소가 step보다 멀리 있으면 실패
                charge_cnt = 0
                break
            elif charger[m] <= position + K < charger[m + 1]: # 충전소 하나만 지날 수 있으면
                position = charger[m] # 위치를 그 충전소로 옮기고
                charge_cnt += 1 # cnt는 1 증가
            else: # 충전소 2개 이상 지날 수 있으면
                continue # 일단 다음 m으로 넘어가서 판단해보기

        else: # index가 마지막 충전소일 때
            if position + K >= N: # 마지막 충전소 안 가도 골인할 수 있으면 그냥 나가기
                break
            elif charger[m] <= position + K: # 아니면 충전소 한 번 더 들르기
                position = charger[m]
                charge_cnt += 1
            else: # 골인 못하면 0 (근데 사실 이 부분 코드 없어도 통과하긴 했음... 왜?!)
                charge_cnt = 0


    print('#{} {}'.format(t, charge_cnt))

    # 0에서 N까지 가는데 정류장은 charger에 정해져 있고
    # 루프 돌 거 (0, 남은정류장개수)
    # 정류장i < 현재위치 + K < 정류장i+1 이면 정류장i로 이동
    # 만약에 현재위치 + K < 현재 가장 가까운 정류장 면 바로 0 출력
import sys

sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    stops = [0] * (N + 1)                                                   # 충전소 위치를 표시할 리스트
    for charge in charges:                                                  # 충전소가 있는 곳을 1로 지정
        stops[charge] = 1

    p = 0                                                                   # 현재 위치
    cnt = 0                                                                 # 충전한 횟수
    while p <= N:                                                           # 현재 위치가 끝까지 도달하지 않았을 때의 반복문
        if N - p <= K:                                                      # 만약 K만큼의 이동 안에 끝까지 도달할 수 있다면 (종료조건)
            print('#{} {}'.format(idx, cnt))                                # 결과를 출력하고 break
            break

        if 1 in stops[p + 1:p + K + 1]:                                     # K만큼 이동할 거리 안에 충전소가 있다면
            # print(stops[p + 1:p + K + 1])
            p += ''.join(map(str, stops[p + 1:p + K + 1])).rindex('1') + 1  # 가장 멀리 있는 충전소로 현재 위치를 변경
            cnt += 1                                                        # 충전한 횟수가 1 증가
        else:                                                               # 이동 가능한 범위 내에 다른 충전소가 없다면
            print('#{} {}'.format(idx, 0))                                  # 0을 출력하고 break
            break
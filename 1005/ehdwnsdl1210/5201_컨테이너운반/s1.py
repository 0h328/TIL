'''
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반

트럭당 한 개의 컨테이너를 운반 할 수 있고,
트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다!

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고,

A도시에서 B도시로 최대 M대의 트럭이 편도로 한번만 운행
이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면,
옮겨진 화물의 전체 무게가 얼마인지?!?!?!?!?!?!

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도?
컨테이너를 한 개도 옮길 수 없는 경우 0을 출력!
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())            # N : 컨테이너 수 / M : 트럭 수
    weight = list(map(int, input().split()))    # 화물 무게
    load = list(map(int, input().split()))      # 적재 용량

    weight.sort(reverse=True)                   # 내림차순, 큰거부터 비교해서 볼려고 (탐욕?)
    load.sort(reverse=True)

    able = 0        # 가능한 무게 더할 변수

    # 엄두도 못내는 무게 제거용
    for _ in range(len(weight)):            # 화물 갯수만큼 반복 (없어지면 계속 없어지게)
        if weight[0] > load[0]:             # 가장 큰거끼리 비교 무게가 더크면 못담음 걍 제거
            weight.remove(weight[0])        # 없어져도 다시 0자리 비교니까 상관X
        else:                               # 적재가 화물 제일 큰것보다 크면, 나머지보다도 크니까 (내림차순)
            break

    if len(weight) > len(load):             # 화물 수가 더 많다면?
        for i in range(len(load)):          # 적재 수만큼만 돈다(적으니까!)
            if load[i] >= weight[i]:        # 적재가 더 크면 실을 수 있음
                able += weight[i]
            else:                           # 아니면 다음으로
                continue

    # 왜 되지? (tc_2..)
    else:
        for i in range(len(weight)):        # 적재 수가 더 많으니까, 화물 수 만큼 돈다!
            if load[i] >= weight[i]:        # 적재가 더 크면 실을 수 있음
                able += weight[i]
            else:                           # 아니면 다음으로
                continue

    print('#{} {}'.format(tc, able))
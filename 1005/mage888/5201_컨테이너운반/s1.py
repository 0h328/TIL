from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 화물 수, M: 트럭 수

    # 어차피 최댓값을 구해야하기 때문에 화물량 혹은 트럭의 적재량이 높은 수 부터 정렬
    load = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    ans, i, j = 0, 0, 0         # i : 화물의 idx / j : 트럭의 idx
    while i < N and j < M :     # 화물의 idx와 트럭의 idx가 각각 총 수량보다 적을 경우에만 시행
        if load[i] <= truck[j]: # 화물이 적재량보다 작은 경우
            ans += load[i]      # 화물을 계속 더해줌
            j += 1              # 다음 적재량 확인
            # 화물이 적재량보다 큰 경우
        i += 1                  # 이전 화물 버리고, 다음 화물 확인
                                # 화물이 트럭에 적재되었는지 여부 확인
        # if check == N or check == M:    # 총 화물 혹은 총 트럭이 각각의 수 만큼 적재되었다면
        #     break                       # 프로그램 종료

    print('#{} {}'.format(tc, ans))






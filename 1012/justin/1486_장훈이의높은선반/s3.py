def powerset(k, cur_sum):              # 부분집합의 합 활용
    global ans
    if ans < cur_sum:                  # 가지치기
        return
    if N == k:                         # 다 선택 한 경우
        if cur_sum >= B:               # 탑(선반)의 높이 이상인지 체크하고
            if ans > cur_sum:          # (필요한 경우) 최솟값 갱신
                ans = cur_sum
            return
    else:
        # A[k] = 1
        powerset(k+1, cur_sum+heights[k]) # k가 포함된 경우
        # A[k] = 0
        powerset(k+1, cur_sum)            # k가 포함되지 않은 경우

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())              # 점원수, 선반
    heights = list(map(int, input().split()))     # 점원의 키들
    A = [0] * N
    ans = 987654321
    powerset(0, 0)
    result = ans - B
    print('#{} {}'.format(tc, result))
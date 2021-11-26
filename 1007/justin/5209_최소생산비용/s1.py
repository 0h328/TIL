def solve(num, product_num, total_cost):                               # num: 제품 번호, k: 제품 수, total_cost: 비용 합계
    global ans
    if total_cost >= ans:                                              # 최소 비용 초과 -> 가지치기
        return
    if num == product_num:                                             # 모든 배정이 끝난 경우
        # ans = min(ans, cost_sum)
        if total_cost < ans:                                           # (필요한 경우) 최소 비용 갱신
            ans = total_cost
    else:                                                              # 아직 공장 배정이 안된 경우
        for i in range(N):                                             # 공장 후보 i
            if not check[i]:                                           # 배정 안된 공장이면
                check[i] = 1                                           # 배정 완료 처리
                solve(num+1, product_num, total_cost+cost[num][i])     # 다음 제품 확인, 제품 수, total => 현재까지의 비용 + num제품을 i공장에 배정한 경우 드는 비용
                check[i] = 0                                           # i 공장에 다른 제품을 배정하는 경우를 확인하기 위해 복구

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]  # 비용
    ans = 987654321 
    check = [0 for _ in range(N)]                               # 공장 후보군
    solve(0, N, 0)                                              # 제품 번호, 제품 수, 비용 합계
    print('#{} {}'.format(tc, ans))
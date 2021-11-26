def solve(N, sales):
    total = 0
    idx = h_idx = N-1
    while idx >= 0:
        highest_price = sales[h_idx]
        current_price = sales[idx]
        if highest_price > current_price:           # 현재 가격이 최고가보다 작은 경우
            total += highest_price - current_price  # 이때 팔면 차이만큼 이익
        else:           
            h_idx = idx                             # 아니면 최고가 인덱스 갱신
        idx -= 1                                    # 줄여가자
    return total

# 컨셉은 s1과 동일
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))
    ans = solve(N, sales)
    print('#{} {}'.format(tc, ans))
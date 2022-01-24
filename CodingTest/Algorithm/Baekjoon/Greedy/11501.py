import sys
sys.stdin = open('input.txt')

def solution(stock_list):
    res = 0                         # 결과값 저장
    max_profit = stock_list[-1]     # 최대값은 제일 마지막 값으로 저장
    stock_list = stock_list[::-1]   # 역순(뒤에서부터 for문 돌려야 시간 초과 안남)

    for val in stock_list:
        if val > max_profit:        # 현재 값이 최대값보다 큰 경우
            max_profit = val        # 최대값 갱신
        else:                       # 현재 값이 최대값보다 작은 경우
            res += max_profit - val # 이익을 낼 수 있으므로 결과값에 더함

    return res

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    print(solution(stock))
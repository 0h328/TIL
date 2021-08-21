import sys
sys.stdin = open('input.txt')


def millionaire(profit_list):
    result = 0  # 결과값 저장
    max_profit = profit_list[-1]  # 최대값은 제일 마지막 값으로 저장
    profit_list = profit_list[::-1]  # 역순(뒤에서부터 for문 돌려야 시간 초과 안남)

    for value in profit_list:
        if value > max_profit:  # 현재 값이 최대값보다 큰 경우
            max_profit = value  # 최대값 갱신
        else:  # 현재 값이 최대값보다 작은 경우
            result += max_profit - value  # 이익을 낼 수 있으므로 결과값에 더함

    return result


T = int(input())

for test in range(T):
    N = int(input())
    profit = list(map(int, input().split()))

    print('#{}'.format(test+1), millionaire(profit))
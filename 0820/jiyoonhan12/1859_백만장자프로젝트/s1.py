import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    case = int(input()) # not used
    market = list(map(int, input().split()))
    market = market[::-1] # reversed
    max_price = market[0]
    profit = 0
    for i in range(case):
        if max_price > market[i]:
            profit += max_price - market[i]
        else:
            max_price = market[i]
    print('#{} {}'.format(t, profit))
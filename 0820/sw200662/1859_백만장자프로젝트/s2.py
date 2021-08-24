import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    list_price = list(map(int, input().split()))[::-1]
    profit = 0
    sell_price = list_price[0]
    for k in list_price:
        if sell_price > k:
            profit += sell_price - k
        else:
            sell_price = k
    print('#{} {}'.format(i + 1, profit))

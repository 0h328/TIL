import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    list_price = list(map(int, input().split()))
    profit = 0
    while len(list_price) > 0:
        c = max(list_price)
        k = list_price.index(c)
        buy_price = 0
        sell_price = c
        for z in range(k):
            buy_price += list_price[z]
        if k >= 1:
            profit += sell_price * k - buy_price
        list_price = list_price[k + 1:]
    print('#{} {}'.format(i + 1, profit))

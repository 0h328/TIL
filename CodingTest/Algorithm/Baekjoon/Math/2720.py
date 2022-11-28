import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    C = int(input())
    res = []
    coins = [25, 10, 5, 1]
    # for coin in coins:
    #     res.append(C//coin)     # 4, 2, 0, 4
    #     C -= (C//coin) * coin   # 124-100, 24-20, 4-0, 4-4
    #
    # print(*res)

    for coin in coins:
        print(C//coin, end=' ')
        C = C % coin
    print()





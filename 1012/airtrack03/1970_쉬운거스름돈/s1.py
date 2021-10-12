import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8  # 배수 -> 그리디

    for i in range(len(coins)):
        cnt[i] = N // coins[i]
        N %= coins[i]

    print("#{}".format(tc))
    print(*cnt)

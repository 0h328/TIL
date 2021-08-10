import sys

sys.stdin = open("input.txt")

for test in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    surround = [-2, -1, 1, 2]
    ans = 0

    for i in range(2, n - 2):
        cur_height = buildings[i]
        surrounded_buildings = [buildings[i - idx] for idx in surround]
        max_height = max(surrounded_buildings)

        if cur_height - max_height > 0:
            ans += cur_height - max_height

    print("#{} {}".format(test, ans))
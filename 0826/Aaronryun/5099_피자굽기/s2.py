import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N, M = list(map(int, input().split()))

    data = list(map(int, input().split()))

    cnt = [0] * M
    for idx, cheese in enumerate(data):
        for j in range(1, 6):
            if cheese < pow(2, j):
                cnt[idx] = j
                break
    oven = cnt[:N]
    outside = cnt[N:]

    while len(oven) != len(cnt):
        min_data = min(oven)
        for i in range(len(oven)):
            if oven[i] != 0:
                oven[i] = oven[i] - min_data

        oven.append(outside.pop(0))
    print()
    # print(oven)

    # print(cnt)

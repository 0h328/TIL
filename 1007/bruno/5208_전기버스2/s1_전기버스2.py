import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    station = lst[0]                  # 10
    battery = [0] + lst[1:] + [0]     # [0, 2, 1, 3, 2, 2, 5, 4, 2, 1, 0]
    start = now = station
    way = 0
    check = [0] * len(battery)        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        while now > 1:
            now -= 1
            way += 1
            if battery[now] >= way:
                check[now] += 1           # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
                continue
    # print(check)
        now = check.index(1)
        way = 0
        if now == 0:
            break

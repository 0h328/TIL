# 쉬운 거스름돈
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    exchange = [0] * 8

    while N >= 10:
        if N >= 50000:
            N -= 50000
            exchange[0] += 1
        elif N >= 10000:
            N -= 10000
            exchange[1] += 1
        elif N >= 5000:
            N -= 5000
            exchange[2] += 1
        elif N >= 1000:
            N -= 1000
            exchange[3] += 1
        elif N >= 500:
            N -= 500
            exchange[4] += 1
        elif N >= 100:
            N -= 100
            exchange[5] += 1
        elif N >= 50:
            N -= 50
            exchange[6] += 1
        elif N >= 10:
            N -= 10
            exchange[7] += 1
    print('#{}'.format(tc))
    print(*exchange)



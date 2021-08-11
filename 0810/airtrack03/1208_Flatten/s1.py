import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    data = list(map(int, input().split()))
    ans = 0

    while dump > 0:
        dump -= 1
        data[data.index(max(data))] -= 1
        data[data.index(min(data))] += 1

        if max(data) - min(data) <= 1:
            break

    ans = max(data) - min(data)

    print('#{} {}'.format(tc, ans))
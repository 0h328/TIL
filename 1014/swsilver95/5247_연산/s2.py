import sys
sys.stdin = open('input.txt', 'r')
# 시간초과


T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    i = 0
    now = set()
    now.add(N)

    while True:
        tmp = set()
        if M not in now:
            i += 1
            for num in now:
                for k in [num - 1, num + 1, num * 2, num - 10]:
                    if 0 < k <= 1000000:
                        tmp.add(k)
            now = tmp
        else:
            break

    print('#{} {}'.format(tc, i))
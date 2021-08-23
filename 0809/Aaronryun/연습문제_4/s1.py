import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N = list(map(int,input()))
    result = [0] * 10

    for _ in range(len(N)):
        result[N[_]] += 1

    i = 0
    tri = run = 0
    while i < 10:
        if result[i] >= 3:
            result[i] -= 3
            tri += 1
            continue

        if result[i] >= 1 and result[i + 1] >= 1 and result[i + 2] >= 1:
            result[i] -= 1
            result[i + 1] -= 1
            result[i + 2] -= 1
            run += 1
            continue

        i += 1
    if run + tri >= 2:
        print('#{} {}'.format(test + 1, 1))
    else:
        print('#{} {}'.format(test + 1, 0))

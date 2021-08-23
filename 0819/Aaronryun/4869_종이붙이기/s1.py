import sys

sys.stdin = open('input.txt')


def DP(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    return DP(N - 1) + 2 * DP(N - 2)


for test in range(int(input())):
    N = int(input())

    answer = DP(N // 10)
    print('#{} {}'.format(test + 1, answer))

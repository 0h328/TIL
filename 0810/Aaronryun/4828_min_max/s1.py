import sys

sys.stdin = open('input.txt')

T = int(input())


def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


for test in range(T):
    N = int(input())
    args = list(map(int, input().split()))

    BubbleSort(args)

    print('#{} {}'.format(test + 1, args[-1] - args[0]))

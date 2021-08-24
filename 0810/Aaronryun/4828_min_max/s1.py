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

    # BubbleSort(args)

    max_data = 0
    for i in args:
        if max_data<i:
            max_data = i

    min_data = args[0]
    for i in args:
        if min_data>i:
            min_data=i

    answer = max_data-min_data
    print('#{} {}'.format(test + 1, answer))

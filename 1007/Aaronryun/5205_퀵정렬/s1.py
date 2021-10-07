import sys

sys.stdin = open('input.txt')


def quicksort(left, right):
    if left >= right:
        return

    pivot = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and data[pivot] >= data[i]:
            i += 1
        while i <= j and data[pivot] <= data[j]:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
    print(data)

    data[pivot], data[j] = data[j], data[pivot]

    quicksort(left, j)
    quicksort(j + 1, right)


for test in range(1, 1 + int(input())):
    N = int(input())
    data = [*map(int, input().split())]

    left = 0
    right = len(data)
    quicksort(left, right)

    print('#{} {}'.format(test, data[N // 2]))

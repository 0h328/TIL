import sys

sys.stdin = open('input.txt')


def BubbleSort2(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = list(map(int, input().split()))

print(BubbleSort(a))

print(BubbleSort2(a))

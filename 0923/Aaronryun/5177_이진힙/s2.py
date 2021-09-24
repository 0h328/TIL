import sys

sys.stdin = open('input.txt')


def insert(data):
    result.append(data)
    index = len(result) - 1
    while index > 1 and result[index] < result[index // 2]:
        result[index], result[index // 2] = result[index // 2], result[index]
        index //= 2


def sum_heap():
    temp = 0
    index = N // 2
    while index:
        temp += result[index]
        index //= 2
    return temp


for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    result = [0]

    for i in data:
        insert(i)
    answer = sum_heap()

    print('#{} {}'.format(test, answer))

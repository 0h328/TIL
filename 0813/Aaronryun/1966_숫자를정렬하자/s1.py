import sys

sys.stdin = open('input.txt')

T = int(input())


def Bubble(data):
    for i in range(len(data)):
        for j in range(i + 1,len(data)):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
    return data


def Select(data):
    for i in range(len(data)):
        min_i = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_i]:
                min_i = j
        data[i], data[min_i] = data[min_i], data[i]

    return data


for test in range(T):
    N = int(input())

    data = list(map(int, input().split()))

    result = Bubble(data)
    result2 = Select(data)
    print('#{}'.format(test+1),*result)
    # print(Select(data))

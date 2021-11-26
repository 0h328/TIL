# 제한 시간 초과

import sys
sys.stdin = open('input.txt')

T = int(input())

def quicksort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left_data = []
    right_data = []

    for i in range(1, len(data)):
        if data[i] <= pivot:
            left_data.append(data[i])
        else:
            right_data.append(data[i])
    left_sorted = quicksort(left_data)
    right_sorted = quicksort(right_data)


    return [*left_sorted, pivot, *right_sorted]




for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    print('#{} {}'.format(case + 1,quicksort(data)[N//2]))



import sys
sys.stdin = open('input.txt', encoding='UTF8')


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


T = int(input())
for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    sort_arr = selection_sort(arr)
    print('#{}'.format(test+1), end=' ')
    print(*sort_arr)
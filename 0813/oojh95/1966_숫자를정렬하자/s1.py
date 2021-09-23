def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selectsort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def countingsort(arr):
    n = len(arr)
    m = max(arr) + 1
    result = [0 for _ in range(n)]
    cnt = [0 for _ in range(m)]

    for i in range(n):
        cnt[arr[i]] += 1
    for i in range(1, m):
        cnt[i] += cnt[i - 1]

    for i in range(n):
        result[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] -= 1

    return result


import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    bubblesort(arr)
    print('#{}'.format(test_case), end=' ')
    print(*arr, sep=' ')


import sys

sys.stdin = open('input.txt')

T = int(input())

def quick_sort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot-1)
        quick_sort(data, pivot+1, right)

def partition(data, left, right):
    pivot = data[left]
    l_idx, r_idx = left+1, right

    while l_idx <= r_idx:
        while l_idx <= r_idx and data[l_idx] <= pivot:
            l_idx += 1
        while l_idx <= r_idx and data[r_idx] >= pivot:
            r_idx -= 1
        if l_idx < r_idx:
            data[l_idx], data[r_idx] = data[r_idx], data[l_idx]
    data[left], data[r_idx] = data[r_idx], data[left]

    return r_idx

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(data, 0, N-1)

    ans = data[N // 2]

    print('#{} {}'.format(tc, ans))
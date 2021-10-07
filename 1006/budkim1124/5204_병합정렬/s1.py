import sys
sys.stdin = open("input.txt")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    i = 0
    j = 0
    s_list = []

    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            s_list.append(left[i])
            i += 1
        else:
            s_list.append(right[j])
            j += 1

    while i < len(left):
        s_list.append(left[i])
        i += 1

    while j < len(right):
        s_list.append(right[j])
        j += 1

    return s_list


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)

    print("#{} {} {}".format(t+1, result[N//2], cnt))
    # print(result)

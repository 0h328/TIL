import sys

sys.stdin = open('input.txt')


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid_idx = len(a)//2
    left_array = a[:mid_idx]
    right_array = a[mid_idx:]

    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(left, right):
    global cnt
    result = []
    left_index = 0
    right_index = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index == len(left):
        while right_index < len(right):
            result.append(right[right_index])
            right_index += 1

    if right_index == len(right):
        while left_index < len(left):
            result.append(left[left_index])
            left_index += 1

    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list_num = list(map(int, input().split()))
    cnt = 0
    ans_list = merge_sort(list_num)
    print('#{} {} {}'.format(tc,ans_list[len(ans_list)//2],cnt))
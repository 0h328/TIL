import sys
sys.stdin = open('input.txt')


def merge_sort(data):
    if len(data) == 1:
        return data

    left = data[:len(data)//2]
    right = data[len(data)//2:]

    left_data = merge_sort(left)
    right_data = merge_sort(right)

    return merge(left_data, right_data)


def merge(left, right):
    global res
    if left[-1] > right[-1]:
        res += 1
    ans = []
    idx_l = 0
    idx_r = 0
    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] <= right[idx_r]:
            ans.append(left[idx_l])
            idx_l += 1
        else:
            ans.append(right[idx_r])
            idx_r += 1

    while idx_l < len(left):
        ans.append(left[idx_l])
        idx_l += 1

    while idx_r < len(right):
        ans.append(right[idx_r])
        idx_r += 1

    return ans


T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    res = 0
    final = merge_sort(data)

    print('#{} {} {}'.format(case + 1, final[N//2], res))
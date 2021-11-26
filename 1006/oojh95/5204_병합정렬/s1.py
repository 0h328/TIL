import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    sorted_list = []
    L = R = 0

    while len(sorted_list) != len(left) + len(right):
        if left[L] <= right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1
        if R == len(right):
            sorted_list += left[L:]
            cnt += 1
            break
        if L == len(left):
            sorted_list += right[R:]
            break
    return sorted_list


def partition(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    sorted_list = partition(num)
    print('#{} {} {}'.format(tc, sorted_list[N//2], cnt))
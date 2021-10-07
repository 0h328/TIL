import sys
sys.stdin = open('input2.txt')


def partition(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = partition(lst[:mid])
    right = partition(lst[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    result = [0] * (len(left)+len(right))
    i = 0
    left_i = right_i = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_i < len(left) or right_i < len(right):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        elif left_i < len(left):
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < len(right):
            result[i] = right[right_i]
            i += 1
            right_i += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0     # 오른쪽 원소가 먼저 복사되는 경우
    final = partition(L)

    print('#{} {} {}'.format(tc, final[N//2], cnt))
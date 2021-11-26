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

    if left[-1] > right[-1]:
        cnt += 1

    while len(sorted_list) != len(left) + len(right):
        if left[L] <= right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1

        if R == len(right):
            sorted_list += left[L:]
            break

        if L == len(left):
            sorted_list += right[R:]
            break

    return sorted_list

def partition(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = partition(nums[:mid])
    right = partition(nums[mid:])
    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, partition(numbers)[N//2], cnt))
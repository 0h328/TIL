"""
병합 정렬을 이용해 오름차순으로 정렬
단, N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할
=> N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
"""

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


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    result = partition(numbers)
    print('#{} {} {}'.format(tc, result[N//2], cnt))

# runtimeerror가 뜬다. 흠. 재귀로 해보자
# 10개 중 3개가 맞습니다 뜸

import sys
sys.stdin = open('input.txt')

def binary_search_iteration(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    number.sort()
    find_list = list(map(int, input().split()))
    cnt = 0
    for i in range(len(number)):
        target = number[i]
        start = 0
        end = len(number) - 1
        find_val = binary_search_iteration(find_list, target, start, end)

        if find_val == -1:
            pass
        else:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
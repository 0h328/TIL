# 그래도 런타임 에러가 나오네 흠..

import sys
sys.stdin = open('input.txt')

def binary_search_recursion(nums, target, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        if nums[mid] == target:                                             # 값을 찾으면 return 하자
            return mid
        elif nums[mid] > target:                                            # 왼쪽에서 찾고
            return binary_search_recursion(nums, target, start, mid-1)      # end를 mid-1로 설정
        else:                                                               # 오른쪽에서 찾자
            return binary_search_recursion(nums, target, mid+1, end)        # start를 mid+1로 설정
    else:
        return -1                                                           # 못찾으면 -1 반환

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
        find_val = binary_search_recursion(find_list, target, start, end)

        if find_val == -1:
            pass
        else:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
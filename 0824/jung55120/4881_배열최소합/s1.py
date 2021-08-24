import sys
sys.stdin = open('input.txt')

def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    less = []
    more = []
    equal = []
    for a in nums:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    new_list = [list(map(int, input().split())) for _ in range(N)]
    print(quicksort(new_list))

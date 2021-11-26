import sys
sys.stdin = open('input.txt')


def quick_sort(start, end):
    if start < end:
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            while left <= right and nums[left] <= nums[pivot]:
                left += 1
            while left <= right and nums[pivot] <= nums[right]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]

        quick_sort(start, right-1)
        quick_sort(right+1, end)


for tc in range(int(input())):
    N = int(input())

    nums = list(map(int, input().split()))
    quick_sort(0, len(nums)-1)

    print('#{0} {1}'.format(tc+1, nums[N//2]))
    # break

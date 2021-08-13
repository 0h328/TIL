import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def selection_sort(nums):

    # l = len(nums)
    # for i in range(l):
    #     min_num = min(nums[i:])
    #     min_idx = nums.index(min_num)
    #     nums[i], nums[min_idx] = nums[min_idx], nums[i]

    for i in range(len(nums)):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


numbers = list(map(int, input().split()))
print(numbers)
selection_sort(numbers)
print(numbers)
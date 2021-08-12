import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def selection_sort(nums):
    l = len(nums)
    for i in range(l):
        min_num = nums[i]
        for j in range(i, l):
            if nums[j] < min_num:
                nums[i], nums[j] = nums[j], nums[i]


numbers = list(map(int, input().split()))
print(numbers)
selection_sort(numbers)
print(numbers)
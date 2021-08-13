import sys
sys.stdin = open('input.txt')

def Selection_sort(nums):
    for i in range(0, len(nums)-1):
        min = i

        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                min = j

        nums[i], nums[min] = nums[min], nums[i]

    return nums

numbers = list(map(int, input().split()))

print(numbers)

print(Selection_sort(numbers))
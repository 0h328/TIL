import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(len(nums)-1):
        min_num = i
        for j in range(i+1,len(nums)-1):
            if nums[j] < nums[min_num]:
                min_num = j
        nums[i], nums[min_num] = nums[min_num], nums[i]
    return nums


numbers = list(map(int, input().split()))

print(selection_sort(numbers))
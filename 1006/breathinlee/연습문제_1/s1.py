"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(bubble_sort(bubble_nums))


#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(selection_sort(selection_nums))


#3. 카운팅 정렬
def couting_sort(nums):
    cnt_nums = [0] * (max(nums) - min(nums) + 1)
    for num in nums:
        cnt_nums[num - min(nums)] += 1

    sorted_nums = []
    for idx in range(len(cnt_nums)):
        sorted_nums += [idx + min(nums)] * cnt_nums[idx]

    return sorted_nums


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(couting_sort(counting_nums))
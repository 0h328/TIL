"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
bubble_sort(bubble_nums)
print('bubble sort: ', bubble_nums)


#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
selection_sort(selection_nums)
print('selection sort: ', selection_nums)


#3. 카운팅 정렬
def counting_sort(nums):
    cnt_list = [0 for _ in range(max(nums)+1)]
    for num in nums:
        cnt_list[num] += 1

    for idx in range(1, len(cnt_list)):
        cnt_list[idx] += cnt_list[idx-1]

    result_list = [0 for _ in range(len(nums))]
    for idx in range(len(nums)-1, -1, -1):
        result_list[cnt_list[nums[idx]]-1] = nums[idx]
        cnt_list[nums[idx]] -= 1
    return result_list

counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print('counting sort: ', counting_sort(counting_nums))
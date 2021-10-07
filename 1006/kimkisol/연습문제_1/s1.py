"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(bubble_nums):
    for i in range(len(bubble_nums) - 1, 0, -1):
        for j in range(i):
            if bubble_nums[j] > bubble_nums[j + 1]:
                bubble_nums[j + 1], bubble_nums[j] = bubble_nums[j], bubble_nums[j + 1]
    return bubble_nums


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(bubble_sort(bubble_nums))

#2. 선택 정렬
def selection_sort(selection_nums):
    for i in range(len(selection_nums) - 1):
        min_idx = i
        for j in range(i, len(selection_nums)):
            if selection_nums[j] < selection_nums[min_idx]:
                min_idx = j
        selection_nums[i], selection_nums[min_idx] = selection_nums[min_idx], selection_nums[i]
    return selection_nums


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(selection_sort(selection_nums))


#3. 카운팅 정렬
def counting_sort(counting_nums):
    new_counting_nums = [0] * len(counting_nums)
    count_nums = [0] * (max(counting_nums) + 1)
    for num in counting_nums:
        count_nums[num] += 1

    for i in range(1, len(count_nums)):
        count_nums[i] += count_nums[i - 1]

    for i in range(len(counting_nums) - 1, -1, -1):
        num = counting_nums[i]
        new_counting_nums[count_nums[num] - 1] = num
        count_nums[num] -= 1

    return new_counting_nums


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(counting_sort(counting_nums))
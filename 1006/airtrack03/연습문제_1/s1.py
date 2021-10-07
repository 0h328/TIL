"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(nums):
    N = len(nums)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
bubble_sort(bubble_nums)
print(bubble_nums)

#2. 선택 정렬
def selection_sort(nums):
    N = len(nums)
    for i in range(N-1):
        min_val = nums[i]
        min_idx = i
        for j in range(i+1, N):
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
selection_sort(selection_nums)
print(selection_nums)


#3. 카운팅 정렬
def couting_sort(nums):
    N = len(nums)
    sorted_list = [0] * N
    max_val = max(nums)
    cnt = [0] * (max_val + 1)

    for num in nums:
        cnt[num] += 1

    for i in range(1, max_val+1):
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1):
        sorted_list[cnt[nums[i]]-1] = nums[i]
        cnt[nums[i]] -= 1

    return sorted_list


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
counting_nums = couting_sort(counting_nums)
print(counting_nums)
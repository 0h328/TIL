"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if bubble_nums[j] > bubble_nums[j+1]:       # 뒤에 값이 더 크면 교환
                bubble_nums[j], bubble_nums[j+1] = bubble_nums[j+1], bubble_nums[j]


bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
bubble_sort(bubble_nums)
print(bubble_nums)


#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if selection_nums[min_idx] > selection_nums[j]:
                min_idx = j
        selection_nums[i], selection_nums[min_idx] = selection_nums[min_idx], selection_nums[i]


selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
selection_sort(selection_nums)
print(selection_nums)


#3. 카운팅 정렬
def counting_sort(nums):
    global answer
    
    for num in nums:            # 각 숫자 카운트
        counted_li[num] += 1
    
    for idx in range(len(counted_li)):
        if counted_li[idx]:
            answer += [idx] * counted_li[idx]


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
answer = []
counted_li = [0] * (max(counting_nums) + 1)
counting_sort(counting_nums)
print(answer)
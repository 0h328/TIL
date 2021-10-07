"""
연습 문제1. 정렬 복습
"""
#1. 버블 정렬
def bubble_sort(nums):
    N = len(nums)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums

bubble_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(bubble_nums)
print(bubble_sort(bubble_nums))

print('-------------------------------------')

#2. 선택 정렬
def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums), 1):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

selection_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(selection_nums)
selection_sort(selection_nums)
print(selection_nums)

print('-------------------------------------')

#3. 카운팅 정렬
def couting_sort(nums):
    N = len(nums)
    count = [0] * 10000                  # 해당 숫자가 몇 번나왔는지 카운트(배열 요소의 최댓값보다 크게 설정)
    sorted_nums = [0] * N

    for num in nums:
        count[num] += 1                  # count 배열의 인덱스 위치에 1개씩 카운트

    for i in range(1, len(count)):       # 최소 ~ 최대 사이의 범위가 클 수록 비효율적
        count[i] = count[i-1] + count[i] # 이전 인덱스에 위치한 값에 현재 값을 더한 값을 쌓아가자

    for num in nums:                     # 2가 나오면
        sorted_nums[count[num]-1] = num  # count[2] -> 3-1 -> 2 -> 2가 갈 자리는 sorted_nums의 index 2번 위치
        count[num] -= 1                  # 동일한 숫자가 나오면 하나 앞에 위치
    return sorted_nums


counting_nums = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(counting_nums)
print(couting_sort(counting_nums))
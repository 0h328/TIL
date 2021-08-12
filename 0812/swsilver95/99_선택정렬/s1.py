import sys

sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))

def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i                                     # 피벗
        for j in range(i + 1, len(nums)):               # i보다 뒤쪽의 원소들만 조사
            if nums[min_idx] > nums[j]:                 # 더 작은 원소가 나타났다면
                min_idx = j                             # 작은 원소 기준으로 인덱스를 바꾸고
        nums[i], nums[min_idx] = nums[min_idx], nums[i] # 가장 작은 원소를 피벗 자리와 변경
    return nums

print(numbers)
print(selection_sort(numbers))
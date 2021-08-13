import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(len(numbers)-1):
        small = i
        for k in range(i+1, len(numbers)): # 최소값 선택
            if nums[small] > nums[k]:
                small = k

        nums[i], nums[small] = nums[small], nums[i] # 자리 맨 앞으로 바꿈

numbers = list(map(int, input().split()))
print(numbers)
selection_sort(numbers)
print(numbers)
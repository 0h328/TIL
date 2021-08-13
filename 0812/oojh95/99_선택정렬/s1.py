def selection_sort(nums):
    for i in range(len(nums) - 1):  #마지막요소의 앞에서 마지막요소와 비교할 것이므로
        min_idx = i # 기준이 되는 i지점의 인덱스를 최소값으로 두자
        for j in range(i + 1, len(nums)):   # 기준점 뒤의 요소들 중 최소값을 찾을 예정이므로
            if nums[min_idx] > nums[j]:
                min_idx = j #최소값의 인덱스 저장
        nums[i], nums[min_idx] = nums[min_idx], nums[i] # 배열중 가장 작은값과 스왑
    return nums



import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))
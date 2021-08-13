import sys
sys.stdin = open('input.txt')

def selection_sort(nums):
    for i in range(len(nums)-1):                      # 마지막꺼는 굳이 확인할 필요가 없어서 -1을 해주나?
        min_idx = i                                   # i를 min_num에 넣기
        for j in range(i+1, len(nums)):               # i보다 1 큰 수부터
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

numbers = list(map(int, input().split()))
print(selection_sort(numbers))
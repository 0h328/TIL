import sys
sys.stdin = open('input.txt')

# thought process:
# 주어진 리스트에서 최솟값 찾고
# 그 값을 리스트 맨 앞에 위치한 값과 교환
# 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

# def selection_sort(nums):
#     for i in range(len(nums)-1):            # 마지막 값은 최솟값이 본인이니까 스킵, 고로 len(nums)-1
#         minV = i                            # 맨 앞을 제일 작다고 가정
#         for j in range(i+1, len(nums)):     # nums[i]의 다음 원소값부터와 비교
#             if nums[minV] > nums[j]:        # 기존의 최솟값보다 작으면
#                 minV = j                    # 최솟값 바꾸고
#         nums[i], nums[minV] = nums[minV], nums[i]   #구간에서의 최솟값을 맨 앞으로
#     return nums

def selection_sort(nums):
    for i in range(len(nums)-1):
        min_val = i
        for j in range(i+1, len(nums)):
            if nums[min_val] > nums[j]:
                min_val = j
        nums[i], nums[min_val] = nums[min_val], nums[i]
    return nums



numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))
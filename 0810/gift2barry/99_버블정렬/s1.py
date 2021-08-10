import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split(', ')))

# for i in range(0, len(nums)-1):
#     for j in range(0, len(nums)-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

# 인풋 리스트의 마지막 값들을 하나씩 줄여나간다
for i in range(len(nums)-1, 0, -1):
    # 정리된 리스트를 돌아가며
    for j in range(i):
        # 현재인덱스값이 다음 인덱스값보다 크면
        if nums[j] > nums[j+1]:
            # 자리를 바꾼다
            nums[j], nums[j + 1] = nums[j+1], nums[j]

print(nums)

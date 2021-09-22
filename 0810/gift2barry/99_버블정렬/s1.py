import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split(', ')))

# for i in range(0, len(nums)-1):
#     for j in range(0, len(nums)-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

# 소요 시간: 58분
# thought process:
# 인풋 리스트를 인덱싱으로 처음부터 끝까지 돌아가며
# 현재 인덱스와 바로 뒤 인덱스중에 작은값을 앞으로 보내며
# 인덱싱 하나의 사이클이 끝날 때 마다 마지막 인덱스의 요소를 인덱싱에서 배재하며
# 인덱싱을 할 더이상 없어질 때 까지 반복

# 인풋 리스트의 마지막 값들을 하나씩 줄여나간다
for i in range(len(nums)-1, 0, -1):
    # 정리된 리스트를 돌아가며
    for j in range(i):
        # 현재인덱스값이 다음 인덱스값보다 크면
        if nums[j] > nums[j+1]:
            # 자리를 바꾼다
            nums[j], nums[j + 1] = nums[j+1], nums[j]

print(*nums)

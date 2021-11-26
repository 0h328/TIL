# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

# 맨 앞에 위치한 수는 len(nums)만큼 비교 필요 한개 뒤에 위치하면서 비교 수 줄어듬
for i in range(len(nums) - 1, 0, -1):
    # 맨 앞에 위치한 수부터 비교
    for j in range(i):
        # j 번째와 j + 1 크기 비교 후, 값 변경
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)

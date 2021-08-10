import sys
sys.stdin = open('input.txt')

# 패작1
# Though process:
# 가로 빈칸 = 낙차
# bubble sort 로 가장 높은 세로값 찾고,
# for height in range(가장높은세로값) 로 해당 height 과
# 같거나 높은 블록 숫자를 각 각 field_width 에서 뺀다.
# 해당 값들을 하나의 리스트에 저장.
# 모든 값들이 모이면, 해당 리스트에서 가장 높은 숫자를 반환

# def init():
#     N = int(input())
#
#     for _ in range(N):
#         field_width = int(input())
#         nums = list(map(int, input().split()))
#         temp = []
#         highest_block = max(nums)
#
#         for height in range(highest_block):
#             filled_block = 0
#             for block in nums:
#                 if height <= block:
#                     filled_block += 1
#             empty_block = field_width - filled_block
#             temp.append(empty_block)
#         print(max(temp))

            # bubble sort 실패..
            # for j in range(field_width):
            #     #bubble sort 로 가장 높은 세로값 확인
            #     if nums[j] > nums[j+1]:
            #         nums[j], nums[j+1] = nums[j+1], nums[j]
            # highest = nums[len(nums)]
            # print(highest)

# init()


Thought process:

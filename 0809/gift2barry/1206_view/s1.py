import sys
sys.stdin = open('input.txt')

# 패작2
# thought process:
# 앞&뒤 두개 인덱스가 현재 인덱스보다 작을때
# 네개의 인덱스값중에 가장 큰 값을 찾아서
# 현재 인덱스값에서 빼준다 = 전망 값.
# 인덱싱으로 돌아가면서 전망값을 jeonmang 에 축적

# 문제점:
# 답은 맞게 나오는데, input.txt 에서 전체 값들 불러오질 못함

N = int(input())
nums = list(map(int, input().split()))
jeonmang = 0

for i in range(N):
    # 앞&뒤 두개 인덱스가 현재 인덱스보다 작을때
    if nums[i] > nums[i-1] and nums[i] > nums[i-2] and nums[i] > nums[i+1] and nums[i] > nums[i+2]: #
        # 네개의 인덱스값중에 가장 큰 값을 찾아서
        # 패작 코드 ↓
        # temp = [nums[i-1], nums[i-2], nums[i+1], nums[i+2]]
        # for j in range(len(temp)):
        #     if temp[j] > temp[j+1]:
        #         temp[j], temp[j+1] = temp[j+1], temp[j]
        # highest_num = temp[len(temp)]
        # 성공작 ↓
        highest_num = max(nums[i - 1], nums[i - 2], nums[i + 1], nums[i + 2])
        # 현재 인덱스값에서 빼준다 = 전망 값.
        room = nums[i] - highest_num
        # 인덱싱으로 돌아가면서 모든 전망값을 jeonmang 에 축적
        jeonmang += room

print(jeonmang)




# 패작1
# thought process:
# 두개 앞에 인덱스 값들이 나보다 작을때 차를 구하고
# 두개 뒤에 인덱스 값들이 나보다 작을때 차를 구하고
# 그 두가지를 비교해서 더 작은쪽이 확보된 전망
# (맨 앞에 경우는 뒤에 두개 인덱스값들만 확인)
# (맨 뒤에 경우는 앞에 두개 인덱스 값들만 확인)

# 문제점:
# 맨 앞과 맨 뒤인덱스의 경우를 따로 관리할 필요x
# 코딩 자체가 틀렸음.
# 고로, 새로하는게 좋다 판단.

# for i in range(N):
#      total = 0
#      temp = []
#      if i == 0 and nums[i] > nums[i+1] and nums[i+2]:
#          if nums[i+1] > nums[i+2]:
#              room = nums[i] - nums[i+1]
#              total += room
#          else:
#              room = nums[i] - nums[i+2]
#              total += room
#
#      elif i == N and nums[i] > nums[i-1] and nums[i-2]:
#          if nums[i-1] > nums[i-2]:
#              room = nums[i] - nums[i-1]
#              total += room
#          else:
#              room = nums[i] - nums[i-2]
#              total += room
#
#      elif nums[i] > nums[i-1] and nums[i] > nums[i-2] and nums[i] > nums[i+1] and nums[i] > nums[i+2]:
#          temp.append(nums[i-2])
#          temp.append(nums[i-1])
#          temp.append(nums[i+1])
#          temp.append(nums[i+2])
#          max_num = max(temp)
#          total += max_num
#
#      print(total)




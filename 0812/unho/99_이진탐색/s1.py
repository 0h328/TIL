import sys
sys.stdin = open('input.txt')



# 이진 탐색 기본

def binary_search(numbers, target):
   high = len(numbers)-1               # 가장 마지막 인덱스
   low = 0                             # 가장 처음 인덱스

   while low <= high:                  # 가장 낮은 인덱스가 높은 인덱스를 지나치면 종료
      mid = (high + low)//2            # 두 인덱스의 가운데 인덱스 탐색, 정수형을 위해 몫만 구함

      if numbers[mid] == target:       # 인덱스의 값이 타겟 값이랑 같으면 True 반환
         return True
      elif numbers[mid] > target:      # 인덱스의 값이 타겟 값보다 크면 가장 높은 인덱스를 현재 인덱스 - 1
         high = mid - 1
      else:                            # 인덱스의 값이 타겟 값보다 작으면 가장 작은 인덱스를 현재 인덱스 + 1
         low = mid + 1


   return False

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
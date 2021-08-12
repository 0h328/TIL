import sys
sys.stdin = open("input1.txt")

# 이진 탐색 기본

def binary_search(numbers, target):
   start = 0                        # start를 0으로 초기화
   end = len(numbers) - 1           # end를 마지막 인덱스 값으로 초기화
   mid = 0                          # while에 mid를 쓰기 위해 mid를 0으로 초기화

   while(end > mid):                # end가 mid보다 클 동안 반복
      mid = (start + end) // 2      # mid를 start와 end의 중간 값으로 초기화

      if target < numbers[mid]:     # tartget이 numbers의 mid 인덱스 값보다 작으면
         end = mid - 1              # end를 mid - 1로 만듦
      elif target > numbers[mid]:   # tartget이 numbers의 mid 인덱스 값보다 크면
         start = mid + 1            # start를 mid + 1로 만듦
      elif target == numbers[mid]:  # tartget이 numbers의 mid 인덱스 값이랑 같으면
         return True                # True 반환
   return False                     # while이 끝나면 False 반환

numbers = list(map(int, input().split()))
print(binary_search(numbers, 1)) # True
print(binary_search(numbers, 10)) # False
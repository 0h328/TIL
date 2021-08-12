# 이진 탐색 기본
import sys
sys.stdin = open('input.txt')


def binary_search(numbers, target):
   low = 0
   high = len(numbers)-1
   while low <= high:
       mid = (low + high) // 2
       if numbers[mid] > target:
           high = mid -1
       elif numbers[mid] < target:
           low = mid + 1
       else:
           return True
   return False



numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
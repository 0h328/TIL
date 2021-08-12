import sys
sys.stdin = open('input.txt')

# 이진 탐색 기본

def binary_search(numbers, target):
   start = 0
   end = len(numbers) -1

   while start < end:
       middle = (start + end) // 2
       if numbers[middle] < target:
           start = middle+1
       elif numbers[middle] == target:
           return True
       else:
           end = middle -1

   return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
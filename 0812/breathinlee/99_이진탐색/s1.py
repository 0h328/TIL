import sys
sys.stdin = open("input.txt")

def binary_search(numbers, target):
   start = 0
   end = len(numbers) - 1
   while start - end <= 0:
       mid = (start + end) // 2
       if numbers[mid] == target:
           return True
       elif numbers[mid] > target:
           end = mid - 1
       else:
           start = mid + 1
   return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
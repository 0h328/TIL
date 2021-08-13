import sys
sys.stdin = open('input.txt')
# 이진 탐색 기본

def binary_search(numbers, target):
   start = 0
   end = len(numbers) - 1
   while start <= end:
       middle = (start + end) // 2
       if target == numbers[middle]:
           return True
       elif target < numbers[middle]:
           end = middle - 1
       else:
           start = middle + 1

   return False

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False

# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    middle = (start + end) // 2
    if start > end:
        return False
    if target == numbers[middle]:
        return True
    elif target < numbers[middle]:
        return recursive_binary_search(numbers[start:middle], target)
    else:
        return recursive_binary_search(numbers[middle + 1:end], target)

# numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
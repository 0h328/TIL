# 이진 탐색 기본

import sys
sys.stdin = open('input.txt')

def binary_search(numbers, target):
    numbers.sort()
    left = 0
    right = len(numbers) - 1

    while left <= right:
       mid = (left + right) // 2
       if numbers[mid] == target:
           return True
       elif numbers[mid] > target:
           right = mid - 1
       else:
           left = mid + 1

    return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
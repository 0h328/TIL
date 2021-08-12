# 이진 탐색 재귀
import sys
sys.stdin = open('input.txt')

def recursive_binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if target == numbers[mid]:
            return True
        elif target < numbers[mid]:
            return recursive_binary_search(numbers[:mid], target)
        elif numbers[mid] < target:
            return recursive_binary_search(numbers[mid+1:], target)

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 9)) # True
print(recursive_binary_search(numbers, 10)) # False
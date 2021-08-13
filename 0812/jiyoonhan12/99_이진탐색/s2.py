# 이진 탐색 재귀

import sys
sys.stdin = open('input.txt')

def recursive_binary_search(numbers, target):
    if len(numbers) == 1 and numbers[0] != target:
        return False
    else:
        left = 0
        right = len(numbers) - 1
        mid = (left + right) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] > target:
            return recursive_binary_search(numbers[:mid], target)
        else:
            return recursive_binary_search(numbers[mid+1:], target)


numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
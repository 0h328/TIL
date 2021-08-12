import sys

sys.stdin = open('input.txt')

def recursive_binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    if left > right:
        return False
    else:
        mid = (left + right) // 2
        if target == numbers[mid]:
            return True
        elif numbers[mid] < target:
            return recursive_binary_search(numbers[mid + 1:right + 1], target)
        else:
            return recursive_binary_search(numbers[left:mid - 1], target)

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
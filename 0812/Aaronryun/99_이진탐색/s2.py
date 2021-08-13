import sys

sys.stdin = open('input.txt')


# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == target:
            return True
        else:
            return False

    if len(numbers) == 0:
        return False

    mid = len(numbers) // 2
    if target == numbers[mid]:
        return True

    if target > numbers[mid]:
        return recursive_binary_search(numbers[mid + 1:], target)
    else:
        return recursive_binary_search(numbers[:mid], target)


numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5))  # True
print(recursive_binary_search(numbers, 10))  # False

import sys

sys.stdin = open('input.txt')


# 이진 탐색 기본

def binary_search(numbers, target):
    numbers.sort()
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return True

        elif numbers[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5))  # True
print(binary_search(numbers, 10))  # False

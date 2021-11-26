# 이진 탐색 기본
import sys
sys.stdin = open('input.txt')


def binary_search(numbers, target):

    start = 0
    end = len(numbers)-1

    while start <= end:
        middle = (start + end) // 2

        if numbers[middle] == target:
            return True
        elif numbers[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return False


numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False


def recursive_binary_search(numbers, target):

    middle = (len(numbers) - 1) // 2

    if middle < 0:
        return False

    if numbers[middle] == target:
        return True

    elif numbers[middle] < target:
        return recursive_binary_search(numbers[middle+1:], target)

    else:
        return recursive_binary_search(numbers[:middle], target)


numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False

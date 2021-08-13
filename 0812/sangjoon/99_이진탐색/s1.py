import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


# 이진 탐색 기본
def binary_search(numbers: list, target: int):
    s, e = numbers[0], numbers[-1]

    while s <= e:
        mid = (s + e) // 2
        if target == numbers[mid]:
            return True
        elif target > numbers[mid]:
            s = mid + 1
        else:
            e = mid - 1

    return False


# 이진 탐색 재귀
def recursive_binary_search(numbers: list, target: int, start: int, end: int):
    if start > end:
        return False
    else:
        mid = (start + end) // 2

        if target == numbers[mid]:
            return True
        elif target > numbers[mid]:
            return recursive_binary_search(numbers, target, mid + 1, end)
        else:
            return recursive_binary_search(numbers, target, start, mid - 1)


numbers = list(map(int, input().split()))
numbers.sort()

print(binary_search(numbers, 5))  # True
print(binary_search(numbers, 10))  # False

start, end = numbers[0], numbers[-1]
print(recursive_binary_search(numbers, 5, start, end))  # True
print(recursive_binary_search(numbers, 10, start, end))  # False

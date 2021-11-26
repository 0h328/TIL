import sys
sys.stdin = open('input.txt')


def ordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
        if numbers[i] > target:
            return False
    else:
        return False


numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False


def unordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
    else:
        return False


numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
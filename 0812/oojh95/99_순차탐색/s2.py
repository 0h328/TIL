def ordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
        if numbers[i] > target:
            return False
    else:
        return False

# 정렬되지 않은 리스트
def unordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
    else:
        return False
import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))
print(ordered_sequential_search(numbers, 8))  # True
print(ordered_sequential_search(numbers, 94))  # False
print(unordered_sequential_search(numbers_2, -9))  # True
print(unordered_sequential_search(numbers_2, 74))
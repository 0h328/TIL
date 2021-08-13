def binary_search(numbers, target):
    N = len(numbers)
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if target > numbers[middle]:
            start = middle + 1
        elif target < numbers[middle]:
            end = middle - 1
        else:
            return True
    return False
import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
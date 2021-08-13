import sys
sys.stdin = open('input.txt')

def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        middle = (start + end) // 2
        if numbers[middle] == target:
            return True
        elif numbers[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return False

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
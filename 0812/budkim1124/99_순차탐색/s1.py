import sys
sys.stdin = open('input.txt')

def unordered_sequential_search(numbers, target):
    i = 0
    while i < len(numbers) and numbers[i] != target:
        i = i+1

    if i <len(numbers):
        return True
    else:
        return False

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, -9))  # True
print(unordered_sequential_search(numbers, 94))  # False
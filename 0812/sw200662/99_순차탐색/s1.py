import sys
sys.stdin = open('input.txt')

def ordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return True
        if i == len(numbers) - 1:
            return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
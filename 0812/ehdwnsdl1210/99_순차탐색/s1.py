import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))

def ordered_sequential_search(numbers, target):

    i = 0
    while i < len(numbers) and numbers[i] != target:
        i = i + 1
    if i < len(numbers):
        return True
    else:
        return False

print(ordered_sequential_search(numbers, -9))
print(ordered_sequential_search(numbers, 94))
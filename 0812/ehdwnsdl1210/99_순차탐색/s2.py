import sys
sys.stdin = open('input2.txt')

numbers = list(map(int, input().split()))

def unordered_sequential_search(numbers, target):

    i = 0
    numbers.sort()
    while i < len(numbers) and numbers[i] != target:
        i = i + 1
    if i < len(numbers):
        return True
    else:
        return False

print(unordered_sequential_search(numbers, 9))
print(unordered_sequential_search(numbers, 94))
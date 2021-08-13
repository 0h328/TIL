import sys
sys.stdin = open('input2.txt')

def unordered_sequential_search(numbers, target):
    for i in range(len(numbers)):

        if numbers[i] == target:
            return True

    return False

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
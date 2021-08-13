import sys
sys.stdin = open('input.txt')

def ordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] > target :
            return False

        if numbers[i] == target:
            return True

    return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, 1))  # True
print(ordered_sequential_search(numbers, 94))  # False
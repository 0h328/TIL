import sys
sys.stdin = open('input.txt')


def ordered_sequential_search(numbers, target):
    for num in numbers:
        if target > num:
            break
        elif target < num:
            continue
        else:
            return True
    return False


numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False

def unordered_sequential_search(numbers, target):
    idx = 0
    while idx < len(numbers):
        if numbers[idx] == target:
            return True
            break
        else:
            idx += 1
    return False

print(unordered_sequential_search(numbers, -9))  # True
print(unordered_sequential_search(numbers, 94))  # False
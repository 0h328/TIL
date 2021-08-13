import sys
sys.stdin = open("input.txt")

def recursive_binary_search(numbers, target, start, end):
    mid = (start + end) // 2

    if start - end > 0:
        return False
    else:
        if numbers[mid] == target:
            return True
        elif numbers[mid] > target:
            return recursive_binary_search(numbers, target, start, mid - 1)
        else:
            return recursive_binary_search(numbers, target, mid + 1, end)


numbers = list(map(int, input().split()))
N = len(numbers)
print(recursive_binary_search(numbers, 5, 0, N-1))  # True
print(recursive_binary_search(numbers, 10, 0, N-1))  # False
import sys
sys.stdin = open('input2.txt')

numbers = list(map(int, input().split()))

def recursive_binary_search(numbers, start, end, target):
    if start > end:
        return False

    else:
        middle = (start + end) // 2
        if target == numbers[middle]:
            return True
        elif target < numbers[middle]:
            return recursive_binary_search(numbers, start, middle - 1, target)
        elif target > numbers[middle]:
            return recursive_binary_search(numbers, middle + 1, end, target)

print(recursive_binary_search(numbers, 1, 9, 5))
print(recursive_binary_search(numbers, 1, 9, 10))
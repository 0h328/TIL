import sys
sys.stdin = open('input.txt')

# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    middle = (start + end) //2
    if not(start <= end):
        return False
    if numbers[middle] == target:
        return True
    elif numbers[middle] < target:
        return recursive_binary_search(numbers[middle+1:],target)
    else:
        return recursive_binary_search(numbers[:middle],target)
    return False

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False

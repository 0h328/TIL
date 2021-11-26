import sys
sys.stdin = open('input.txt')

def binary_search(numbers, target):
    numbers.sort()
    start = 0
    end = len(numbers) - 1

    while start <= end:
        div = (start + end) // 2
        if numbers[div] == target:
            return True
        elif numbers[div] > target:
            end = div - 1
        else:
            start = div + 1
    return False

arr = list(map(int, input().split()))
print('not recursion')
print(binary_search(arr, 5))
print(binary_search(arr, 10))


def recursive_binary_search(numbers, target):
    if len(numbers) == 0: # base case
        return False

    else:
        start = 0
        end = len(numbers) - 1
        div = (start + end) // 2
        if numbers[div] == target:
            return True
        elif numbers[div] > target:
            return recursive_binary_search(numbers[:div], target)
        else:
            return recursive_binary_search(numbers[div+1:], target)

print(recursive_binary_search(arr, 5))
print(recursive_binary_search(arr, 10))
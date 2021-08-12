# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    mid = len(numbers)//2
    if len(numbers) == 0:
        return False
    if numbers[mid] == target:
        return True
    elif numbers[mid] > target:
        return recursive_binary_search(numbers[mid+1:], target)
    else:
        return recursive_binary_search(numbers[:mid], target)

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
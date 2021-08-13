import sys
sys.stdin = open('input.txt')



# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    # Base Case
    if len(numbers) == 1 and numbers[0] != target:              # 리스트 길이가 1인데, 값이 다르면 False
        return False

    high = len(numbers) - 1
    low = 0
    mid = (high + low)//2

    if numbers[mid] == target:
        return True
    elif numbers[mid] > target:
        return recursive_binary_search(numbers[:mid], target)
    elif numbers[mid] < target:
        return recursive_binary_search(numbers[mid+1:], target)



numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
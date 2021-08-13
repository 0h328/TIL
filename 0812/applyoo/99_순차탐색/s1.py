import sys
sys.stdin = open('input.txt')

def unordered_sequential_search(numbers, target):
    for i in numbers:
        if i == target:
            return True
    return False

arr = list(map(int, input().split()))

print(unordered_sequential_search(arr, -9))
print(unordered_sequential_search(arr, 94))
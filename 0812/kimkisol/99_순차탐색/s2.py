import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

def ordered_sequential_search(numbers, target):
    for idx in range(len(numbers)):
        if target == numbers[idx]:
            return True
    return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, 9))  # True
print(ordered_sequential_search(numbers, 94))  # False


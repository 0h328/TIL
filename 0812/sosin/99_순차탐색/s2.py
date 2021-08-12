import sys
sys.stdin = open('input.txt')

# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    for n in numbers:
        if n == target:
            return True
    return False
    
numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, -9))  # True
print(unordered_sequential_search(numbers, 94))  # False
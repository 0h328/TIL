# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False

import sys
sys.stdin = open('input2.txt')

def unordered_sequential_search(numbers, target):
    i = 0

    # list 길이 벗어나거나 그 전에 target 숫자 찾았을 경우 빠져나감
    while i < len(numbers) and numbers[i] != target:
        i += 1

    if i < len(numbers): # target 숫자 찾아서 빠져나간 경우
        return True
    else: # list 길이 초과해서 빠져나간 경우
        return False

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 2))  # True
print(unordered_sequential_search(numbers, 94))  # False
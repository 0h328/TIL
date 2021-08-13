import sys
sys.stdin = open('input.txt')
# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False

def unordered_sequential_search(numbers, target):
    i = 0
    while i < len(numbers) and numbers[i] < target: # 타겟보다 작을때까지만 i + 1
        i += 1
    if i < len(numbers) and numbers[i] == target:   # 멈춘 요소의 다음값이 타겟과 같음
        return True                              # 안에 있음
    else:                                   # i가 길이 이상 or 다음값이 타겟과 다름
        return False                    # 안에 없음

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 5))  # True
print(unordered_sequential_search(numbers, 94))  # False
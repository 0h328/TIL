import sys
sys.stdin = open('input2.txt')

# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    i = 0
    while i < len(numbers) and numbers[i] != target:  # 타겟과 같아지기 전까지 i +1
        i += 1
    if i < len(numbers):                              # i가 길이 내 => 안에 있음
        return True
    else:                                             # i가 길이 이상 => 없음
        return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -1))  # True
print(ordered_sequential_search(numbers, 94))  # False
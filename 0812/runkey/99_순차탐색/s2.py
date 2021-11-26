import sys
sys.stdin = open("input2.txt")

# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    for num in numbers:         # numbers의 원소들을 반복
        if num == target:       # num이 tartget과 같으면
            return True         # True 반환
    return False                # 반복이 끝나면 False 반환

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
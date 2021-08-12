import sys
sys.stdin = open("input1.txt")

# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    for num in numbers:     # numbers의 요소를 하나씩 봄
        if num > target:    # num이 target보다 크면 (정렬 되어 있기에 더 이상 찾을 필요X)
            return False    # False 반환

        if num == target:   # num이 target과 같으면
            return True     # True 반환
    return False            # Target이 num의 숫자들보다 커서 반복을 다 돌면 False 출력

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
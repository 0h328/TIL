import sys
sys.stdin = open('input.txt')

# 정렬된 순차 탐색
# 1. 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    # index
    pos = 0
    # 값을 찾으면 True로 바뀌는 flag variable
    found = False

    # 끝까지 검색 x AND target이 발견되지 않을 때까지 반복 수행
    while pos < len(numbers) and not found:
        # 만약 pos에 해당하는 값이 내가 찾고자 하는 값(target)이면
        if numbers[pos] == target:
            # 발견
            found = True
        # 아니라면 
        else:
            # index를 증가 시키자
            pos += 1

    return found


numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, -9))  # True
print(unordered_sequential_search(numbers, 94))  # False

# 2. 검색 대상을 찾는 리스트가 정렬되어 있다고 가정
# input을 수정하고 확인!
def ordered_sequential_search(numbers, target):
    pos = 0
    found = False
    stop = False

    # 끝까지 검색 x AND target 발견 X AND 현재 pos의 value가 target보다 작을 때(정렬)
    while pos < len(numbers) and not found and not stop:
        # 만약 해당하는 위치에 내가 찾고자 하는 값이 있다면
        if numbers[pos] == target:
            # 찾았다!
            found = True
        else:
            # 정렬되어 있기 때문에 target을 절대로 찾을 수 없음
            if numbers[pos] > target:
                # 반복을 끝내자 -> break도 가능
                stop = True
            # 아니라면
            else:
                # 다음으로 이동 이동
                pos += 1
    return found

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, 9))  # True
print(ordered_sequential_search(numbers, 94))  # False
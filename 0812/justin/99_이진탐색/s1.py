#1. 가장 기본적인 이진 탐색
def binary_search(numbers, target):
    start = 0
    # 인덱스의 끝값은 항상 len(numbers)-1
    end = len(numbers) - 1
    found = False

    #1. start와 end가 cross되기 전 그리고 target이 발견되기 전까지
    while start <= end and not found:
        #2. mid 포인트를 잡고
        mid = (start + end) // 2
        #3. 만약에 target이 발견되면 검색 종료
        if numbers[mid] == target:
            found = True
        #4. 발견되지 않으면
        else:
            """
            예시. 
            17 20 26 31 44 54 55 77 93 -> 31 찾기 / mid - 44
            31 < 44 -> 44 - 1 = 43(end)
            start(0) ~ end(43) 사이에 있을 것

            17 20 26 31 44 54 55 77 93 -> 93 찾기 / mid - 44
            93 > 44 -> 44 + 1 = 45(start)
            start(45) ~ end(len(numbers)-1) 사이에 있을 것
            """
            #4-1. 만약에 target 값이 더 작으면 end를 내리고
            if target < numbers[mid]:
                end = mid - 1
            #4-2. 크면 start를 올리자
            else:
                start = mid + 1
    return found

import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False


"""
#2. 재귀 호출을 활용한 이진 탐색 - 분할 정복
def recursive_binary_search(numbers, target):
    if len(numbers) == 0:
        return False
    else:
        mid = len(numbers) // 2
        # 원하는 데이터를 찾은 경우
        if numbers[mid] == target:
            return True
        else:
            # 찾고자 하는 값이 더 작은 경우 -> 오른쪽을 자르자
            if target < numbers[mid]:
                return recursive_binary_search(numbers[:mid], target)
            # 찾고자 하는 값이 더 큰 경우 -> 왼쪽을 자르자
            else:
                # mid point는 포함하면 안되기 때문에 +1
                return recursive_binary_search(numbers[mid+1:], target)

numbers = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
"""
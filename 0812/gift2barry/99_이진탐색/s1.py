# 이진 탐색 기본
import sys
sys.stdin = open('input.txt')
# thought process:
# mid point 찍고
# 기준으로 반 자르고
# target 나올때까지 반복, 안나오면 return False
def binary_search(numbers, target):
    start = 0
    end = len(numbers)

    while start <= target <= end:
        middle = (start + end) // 2  # 이러면 인풋 원소 개수가 짝수여도 정수반환
        if middle == target:
            return True
        else:
            if middle < target:      # 타깃이 가운데 원소값보다 작을 경우
                end = middle         # 가운데가 새로운 end point
            else:
                start = middle       # 아니면 가운데가 새로운 start point

    return False

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
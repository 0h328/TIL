import sys
# from ./99_선택정렬 import s1
# 파일 이름이 숫자로 시작해서 안될지도..
#

sys.stdin = open('input2.txt')


# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False

# thought process:
# 배열 길이 끝까지 순차적으로 인풋값을 찾는다.
# 찾으면 바로 리턴
# 못찾고 원소값이 타깃 넘버보다 크면 바로 return False

# def ordered_sequential_search(numbers, target):
#     for i in range(len(numbers)):
#         if target == numbers[i]:    # 찾으면 함수 끝
#             return True
#         elif numbers[i] > target:   # 원소값이 타깃값을 넘어버리면 함수 끝
#             return False
#     return False                    # 끝까지 못 찾으면 함수 끝


# numbers = list(map(int, input().split()))
# print(ordered_sequential_search(numbers, -9))  # True
# print(ordered_sequential_search(numbers, 94))  # False


# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return True
    return False                    # 루프다 돌아도 없으면 False

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
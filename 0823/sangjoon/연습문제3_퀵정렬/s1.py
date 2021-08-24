# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def quick_sort(nums):
    pass


def partition(arr, start, end):
    pass


def quick_sort(arr, start, end):
    pass


test_case = int(input())

for test in range(1, test_case + 1):
    numbers = list(map(int, input().split()))
    print(quick_sort(numbers, 0, len(numbers) - 1))

    print("#{} {}".format(test, ans))  ## 연습문제3

# - 아래의 입력을 통해 연습하고 추가적으로 `1966_숫자를 정렬하자` 문제를 통해서도 채점 가능

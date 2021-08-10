import sys
sys.stdin = open('input.txt')

# 1. 숫자
num = int(input())
print(num)

# 2. 리스트
nums = list(map(int, input().split()))
print(nums)

# 3. 2차원 리스트
N = int(input())

# my_nums = []
# for _ in range(N):
#     # N번 반복하며 한 줄의 모든 값을 리스트로 만들기
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)
#
# print(my_nums)

# 4. 조금 더 심플한 버전
numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)
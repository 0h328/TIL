import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# #1. 숫자
# num = int(input())
# print(num)
#
# print('#{}'.format(num))
#
# #2. 리스트
# nums = list(map(int, input().split()))
#
# for num in nums:
#     print(num)

# #3. 이차원 리스트
# N = int(input())
#
# my_nums = []
# for _ in range(N):
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)
# print(my_nums)

#4. 심플 버전
numbers = [list(map(int, input().split())) for _ in range(int(input()))]
print(numbers)
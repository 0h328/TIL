import sys
sys.stdin = open('input.txt')

num = int(input())
print(num)

nums = list(map(int, input().split()))
print(nums)

N = int(input())
#
# my_nums = []
# for _ in range(N) :
#     nums = list(map(int, input().split()))
#     my_nums.append(nums)

numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)
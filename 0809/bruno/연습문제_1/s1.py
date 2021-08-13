import sys
sys.stdin = open('input.txt')

num = int(input())
print('#{}'.format(num))

print(list(map(int, input().split())))

#2차원 리스트

N = int(input())
#
# my_num = []
# for _ in range(N):
#     nums = list(map(int, input().split()))
#     my_num.append(nums)
# print(my_num)

numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)
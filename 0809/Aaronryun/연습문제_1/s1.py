import sys
sys.stdin = open('input.txt')

num = int(input())
print(num)

print('#{}'.format(num))

print(list(map(int,input().split())))

N = int(input())

# my_nums = []
# for _ in range(N):
#     nums = list(map(int,input().split()))
#     print(nums)
#     my_nums.append(nums)
# print(my_nums)

nums = [list(map(int,input().split())) for _ in range(N)]
print(nums)
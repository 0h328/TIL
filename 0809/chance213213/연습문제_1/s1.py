import sys
sys.stdin = open('input.txt')


#1.
num = int(input())
#print(num)


print('#{}'.format(num))

# 2. list
print(input())
print(input().split())
print(list(map(int,input().split())))

for num in nums:
    print(num)

#3. 2차원 리스트
N = int(input())

my_nums=[]
for _ in range(N):
    nums = list(map(int,input().split()))
    my_nums.append(nums)
print(my_nums)

numbers = [list(map(int,input().split())) for _ in range(N)]
print(numbers)
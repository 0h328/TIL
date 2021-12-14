import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
res = 0

for num in nums:
    check = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check += 1  #
        if check == 0:
            res += 1
print(res)
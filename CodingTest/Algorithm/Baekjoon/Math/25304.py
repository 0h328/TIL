import sys
sys.stdin = open('input.txt')

price = int(input())
N = int(input())
sum = 0

for i in range(N):
    a, b = map(int, input().split())
    sum += a * b

if price == sum:
    print('Yes')
else:
    print('No')
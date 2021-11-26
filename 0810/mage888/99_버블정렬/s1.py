import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = list(map(int,input().split()))

n = len(numbers)


for i in range(n-1, 0, -1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
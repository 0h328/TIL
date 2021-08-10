import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = [list(map(int,input().split())) for _ in range(N)]


for num in numbers:
    for j in range(2,len(numbers)-2):
        if (num[j]>num[j+1]) and (num[j]>num[j+2]):
            if (num[j+1]>num[j+2]):
                cp1 = num[j+2]-num[j]
            else:
                cp2 = num[j+1]-num[j]
import sys
sys.stdin = open('input.txt')

a = 0
for i in range(1, 5):
    a += int(input())
print(a//60)
print(a%60)
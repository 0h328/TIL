import sys
sys.stdin = open('input.txt')

N = int(input())
grades = list(map(int, input().split()))
fake = []

for grade in grades:
    fake.append((grade/max(grades))*100)

print(sum(fake)/N)
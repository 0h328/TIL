import sys
sys.stdin = open('input.txt')

total = []
people = 0
for i in range(10):
    a, b = map(int, input().split())
    people += b-a
    total.append(people)

print(max(total))
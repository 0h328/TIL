import sys
sys.stdin = open('input.txt')

cnt = set()
for _ in range(10):
    num = int(input())
    cnt.add(num % 42)

print(len(cnt))
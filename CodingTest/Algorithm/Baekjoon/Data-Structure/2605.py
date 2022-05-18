import sys
sys.stdin = open('input.txt')

N = int(input())
students = list(map(int, input().split()))

ans = []

for i in range(N):
    ans.insert(i-students[i], i+1)

print(*ans)
import sys
sys.stdin = open('input.txt')

N = sys.stdin.readline().rstrip()
card = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline().rstrip()
test = list(map(int, sys.stdin.readline().split()))

ans = {}

for i in card:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

for i in test:
    if i in ans:
        print(ans[i], end=' ')
    else:
        print(0, end=' ')
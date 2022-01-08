import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = [-1] * N
stack = []

for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        val, idx = stack.pop()
        res[idx] = arr[i]
    stack.append((arr[i], i))

print(*res)
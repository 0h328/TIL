import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
expect = []
for _ in range(N):
    expect.append(int(sys.stdin.readline()))

expect.sort()

res = 0
for i in range(1, N+1):
    res += abs(i-expect[i-1])
print(res)
import sys

N = int(input())
tmp = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    tmp[num] += 1

for i in range(10001):
    if tmp[i] != 0:
        for _ in range(tmp[i]):
            print(i)
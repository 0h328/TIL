import sys
sys.stdin = open('input.txt')

N = int(input())
lth = len(str(N))-1
cnt = 0

for i in range(lth):
    cnt += 9 * (10 ** i) * (i + 1)

cnt += ((N - (10 ** lth)) + 1) * (lth + 1)

print(cnt)


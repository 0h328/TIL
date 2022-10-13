import sys
sys.stdin = open('input.txt')

s = []
for i in range(7):
    a = int(sys.stdin.readline())
    if a%2 != 0:
        s.append(a)
if s:
    print(sum(s))
    print(min(s))
else:
    print(-1)
import sys
sys.stdin = open('input.txt')

t = int(input())

for num in range(1, t+1):
    l = [list(map(int, input().split())) for _ in range(9)]
    s = {i for i in range(1,10)}
    target = map(set, [*l, *list(zip(*l))])
## 미완

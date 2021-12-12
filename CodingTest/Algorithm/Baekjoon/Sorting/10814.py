import sys
sys.stdin = open('input.txt')

N = int(input())

info = []
for _ in range(N):
    age, name = sys.stdin.readline().strip().split()
    info.append([int(age), name])

info.sort(key=lambda x: x[0])
for res in info:
    print(*res)
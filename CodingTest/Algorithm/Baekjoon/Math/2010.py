import sys
sys.stdin = open('input.txt')

N = int(input())
plug = 0
for _ in range(N):
    plug += int(sys.stdin.readline())

print(plug-N+1)
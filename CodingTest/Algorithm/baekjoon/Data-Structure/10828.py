# 스택
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    com = input().split()

    if 'push' in com:
        stack.append(com[1])
    elif 'top' in com:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif 'size' in com:
        print(len(stack))
    elif 'empty' in com:
        if stack:
            print(0)
        else:
            print(1)
    elif 'pop' in com:
        if stack:
            print(stack.pop())
        else:
            print(-1)






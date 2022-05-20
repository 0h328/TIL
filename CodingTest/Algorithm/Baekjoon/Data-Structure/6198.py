import sys
sys.stdin = open('input.txt')

N = int(input())
b = [int(input()) for _ in range(N)]
stack = []
cnt = 0

for i in range(N):
    while stack and stack[-1] <= b[i]:  # 스택에 있는 빌딩보다 다음 빌딩이 높으면
        stack.pop()                     # 볼수 없으므로 계속 지운다.

    stack.append(b[i])
    cnt += len(stack) - 1   # 자기 자신을 빼야하므로 -1

print(cnt)

import sys
sys.stdin = open('input.txt')

K = list(map(str, sys.stdin.readline().strip()))

stack = []
res = 0

for i in range(len(K)):
    if K[i] == '(':         # (인 상태면 스택에 추가
        stack.append('(')
    elif K[i-1] == ')':     # 이전 인덱스가 )면 막대기의 끝을 잘랐으므로 +1
        stack.pop()
        res += 1
    else:
        stack.pop()
        res += len(stack)   # (가 쌓인 상태에서 현재 인덱스가 )면 하나씩 막대기를 잘랐으므로 +스택의 길이

print(res)
import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    Words = input()
    stack = []
    for k in Words:
        if len(stack) == 0:
            stack.append(k)
        elif k == stack[-1]:
            stack.pop()
        else:
            stack.append(k)
    print('#{} {}'.format(i+1,len(stack)))
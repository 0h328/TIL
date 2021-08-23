import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    stick = input()
    stack = []
    cnt = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append(stick[i])
        elif stick[i] == ')' and stick[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        elif stick[i] == ')':
            stack.pop()
            cnt += 1
    print('#{} {}'.format(case+1, cnt))

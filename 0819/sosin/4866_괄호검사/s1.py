import sys
sys.stdin = open('input.txt')

def sol(sents):
    stack = []
    for s in sents:
        if s in ['{', '(']:
            stack.append(s)
        elif s == '}':
            if stack.pop() != '{':
                return 0
        elif s == ')':
            if stack.pop() != '(':
                return 0
    if stack:
        return 0
    return 1

for T in range(int(input())):
    s = input().rstrip()
    result = sol(s)
    print('#{} {}'.format((T+1), result))

#1 1
#2 1
#3 0
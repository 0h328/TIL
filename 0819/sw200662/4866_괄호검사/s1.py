import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    words = input()
    stack = []
    cnt = 1 # cnt=1일떄 정답, 0일때 실패

    for k in words:
        if k == '(' or k == '{': # 먼저 stack을 쌓는다
            stack.append(k)
        elif len(stack) == 0 and k == ')': #만약 인상태에서 오른쪽 괄호가 나오면 cnt=0, 초기화
            cnt = 0
            break
        elif len(stack) == 0 and k == '}':
            cnt = 0
            break
        elif k == ')': # ) ( 있다면 pop, 없다면 0으로 하고 브레이크
            if stack[-1] == '(':
                stack.pop(-1)
            else:
                cnt = 0
                break
        elif k == '}': # } { 있다면 pop, 없다면 0으로 하고 브레이크
            if stack[-1] == '{':
                stack.pop(-1)
            else:
                cnt = 0
                break
    if len(stack) != 0:
        cnt = 0
    print('#{} {}'.format(i+1,cnt))


import sys
sys.stdin = open('input.txt')

for num in range(10):
    N = int(input())
    data = input()
    stack = []
    result = []

#1. 중위 표현식 -> 후위 표현식
    for i in range(N):

        if data[i] == '+':                      # +인 경우
            while stack:
                if stack[-1] == '(':
                    break
                else:
                    result.append(stack.pop())
            stack.append(data[i])

        elif data[i] == '*':                    # *인 경우
            while stack and stack[-1] =='*':
                result.append(stack.pop())
            stack.append(data[i])

        elif data[i] =='(':
            stack.append(data[i])

        elif data[i] ==')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                result.append(stack.pop())

        else:
            result.append(data[i])

    while stack:
        result.append(stack.pop())

# 후위표현식 -> 계산
    for i in result:
        if i not in ['+','*']:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '*':
                stack.append(int(b)*int(a))
            else:
                stack.append(int(b)+int(a))
    print('#{} {}'.format(num+1, stack.pop()))

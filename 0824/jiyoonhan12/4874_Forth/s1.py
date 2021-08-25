import sys
sys.stdin = open('input.txt')

def forth():
    stack = []
    for i in range(len(line)):
        if line[i].isdigit(): # 숫자면 그냥 append
            stack.append(int(line[i]))
        elif line[i] == '.': # .이면
            if len(stack) == 1: # stack에 하나 남아 있을 때 = 마지막에 . 나올때
                return stack[0]
            else: # 마지막에 나오지 않는 모든 경우
                return 'error'
        else: # 연산기호
            if len(stack) < 2: # 연산 불가능한 경우(숫자가 2개 미만)
                return 'error'
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if line[i] == '+':
                    stack.append(num1+num2)
                elif line[i] == '-':
                    stack.append(num1 - num2)
                elif line[i] == '*':
                    stack.append(num1 * num2)
                elif line[i] == '/':
                    stack.append(num1 // num2)

T = int(input())

for t in range(1, T+1):
    line = list(input().split())
    print('#{} {}'.format(t, forth()))
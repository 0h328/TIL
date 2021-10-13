import sys
sys.stdin = open('input.txt')

def solve(chrs):
    stack = []
    for c in chrs:
        if c in ['+', '-', '*', '/']:
            #에러 확인 방법
            if len(stack) >= 2:
                p2 = stack.pop()
                p1 = stack.pop()
                if c == '+':
                    stack.append(p1+p2)
                elif c == '-':
                    stack.append(p1-p2)
                elif c == '*':
                    stack.append(p1*p2)
                elif c == '/':
                    if p2 == 0:
                        return
                    stack.append(pl//p2)
            else:
                return 'error'
        elif c.isdigit():
            stack.append(int(c))
        elif c == '.':
            #stack의 길이 체크로 에러 확인!!
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'



T = int(input())

for tc in range(1, T+1):
    code = input().split()
    print('#{} {}'.format(tc, solve(code)))
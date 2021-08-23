import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = input()
    data = input() # 중위 표기식
    stack = []
    num = []

    #1. 중위 표현식 -> 후위 표현식
    for char in data:
        if char == '*': # *인 경우 무조건 stack에 추가
            stack.append(char)
        elif char == '+':
            # 이 경우 고려해야 할 사항 : stack이 비어있는지 여부 판단 & stack의 가장 위(top)가 * 연산자인지 확인
            while stack: # 스택이 존재하는 경우 마지막 stack pop해서 num에 push
                num.append(stack.pop())
            stack.append(char) # 스택이 존재하지 않는 경우 무조건 push
        else:
            num.append(char)
    # print(num
    # print(stack)
    while stack:
        num += stack.pop()

    # 2. 후위 표현식 -> 계산
    result = []
    for n in num:
        # print(n)
        if n == '*':
            a = result.pop()
            b = result.pop()
            c = b * a
            result.append(c)
        elif n == '+':
            a = result.pop()
            b = result.pop()
            c = b + a
            result.append(c)
        else:
            result.append(int(n))
    print('#{} {}'.format(tc+1, *result))

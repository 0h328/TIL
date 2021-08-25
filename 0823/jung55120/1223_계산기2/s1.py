# 1. 스택 활용하기
# 2. 후위 표현식으로 만들기
# 3. 계산하기

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    data = input() # 중위 표현식
    print(data)
    stack = []
    my_str = '' # 후위 표현식을 넣을 빈 스트링

    for char in data:
        if char == '*':
            stack.append(char)
        elif char == '+':
            # 빈 리스트인지
            # 만약 '*'이 있다면?
            while stack:
                my_str += stack.pop()
            stack.append(char)
        else:
            my_str += char   # 9+5*2+1+3*3*7*6*9*1

    while stack:  # stack에 남아있는 것들 모두 추가
        my_str += stack.pop()

    print(my_str)

    for char in my_str:
        if char == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)

        elif char == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)

        else:
            stack.append(int(char))

    print('#{} {}'.format(tc, stack[0]))
            # 숫자가 나오면 stack에 넣고...
            # 결론 = 망함
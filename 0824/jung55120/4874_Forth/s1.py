import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_str = list(input().split())
    stack = []
    Forth = ['+', '-', '*', '/']    # Forth라는 사칙연산이 담긴 list를 생성

    try:  # for문을 다 돌려보자!
        if '.' in my_str[0:len(my_str) - 1]:
            result = 'error'
            break
        for char in my_str:
            if char == '.':
                if my_str.index(char) == len(my_str) - 1:
                    result = stack.pop()
                    if len(stack) > 0: # stack에 숫자가 0개가 아니면 error를 반환
                        result = 'error'
                    break
                else:
                    result = 'error'
                    break          # stack의 조건이 맞으면 result에 저장
            elif char == Forth[0]:
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif char == Forth[1]:
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif char == Forth[2]:
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif char == Forth[3]:
                stack.append(stack.pop(-2) // stack.pop(-1))
            else:
                stack.append(int(char))
    except:                     # for문이 다 돌았을 때 IndexError같은 에러가 뜨면 error를 저장
        result = 'error'

    print('#{} {}'.format(tc, result))




    # elif char in Forth:
    #     stack.append(eval(str(stack.pop(-2)) + char + str(stack.pop())))

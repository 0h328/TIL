"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')

my_string = input()
stack = []

for i in range(len(my_string)):
    if my_string[i] == '+' or my_string[i] == '-' or my_string[i] == '*' or my_string[i] == '/':
        stack.append(my_string[i])
    else:
        print(my_string[i], end='')

while stack:
    print(stack.pop(), end='')
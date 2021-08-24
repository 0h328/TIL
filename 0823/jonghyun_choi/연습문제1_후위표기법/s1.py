"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')


my_str = input()
print(my_str)

stack = []

for i in range(len(my_str)):
    if my_str[i] == '+' or my_str[i] == '-' or my_str[i] == '*' or my_str[i] == '/':
        stack.append(my_str[i])
    else:
        print(my_str[i], end='')

while stack:
    print(stack.pop(), end='')
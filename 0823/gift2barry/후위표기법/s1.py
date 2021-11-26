"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')
# 기본 개념 : 중위표현식을 바꾸는법
# my_str = input()
# stack = []
# for i in range(len(my_str)):        # 피연산자면 프린트, 연산자면 스택안에 ㄱ
#     if my_str[i] == '+' or my_str[i] == '-' or my_str[i] == '/' or my_str[i] == '*':
#         stack.append(my_str[i])
#     else:
#         print(my_str[i], end='')
# while stack:
#     print(stack.pop(), end='')      # 이건 좀 간단쓰..

# 1. 중위 표현식을 후위표현식으로 바꾸고, 계산까지 하는게 hws

arr = [1, 2, 3] # 전체집합
N = len(arr)    # 집합의 요소 수
sel = [0] * N   # 해당 요소를 선택

def powerset(idx):
    if idx == N:
        print(*sel)
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
powerset(0)
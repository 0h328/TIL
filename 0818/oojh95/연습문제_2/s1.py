"""
괄호 매칭
1. 괄호의 종류 - [], {}, () -> 단, 이번 연습문제에서는 소괄호만 존재
2. 괄호 매칭의 조건
- 왼쪽 괄호의 개수와 오른쪽 괄호의 '개수'가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 '먼저' 나와야 한다.
 - 괄호 사이에는 포함 관계만 존재한다.
3. 잘못된 사용의 예시
(a(b) -> 괄호 개수
a(b)c) -> 괄호 개수
a{b(c[d]e}) -> 괄호가 올바르게 매칭되지 않음
"""

def push(item):
    stack.append(item)

def pop():
    if is_empty():
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    for i in data:
        if i == '(':
            push(i)
        else:
            if is_empty():
                return False
            pop()
    if is_empty():
        return True
    else:
        return False

import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False

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
    if stack:
        return stack.pop()
    else:
        return

def is_empty():
    if stack:
        return False
    else:
        return True

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    if data[0] == ')':
        return False

    while len(data) > 0:
        if data[0] == '(':              # data의 맨 앞이 '('일 경우
            data = data[1:]             # data의 맨 앞을 제외하고 슬라이싱 한 뒤
            push('(')                   # stack에 '('를 push
        else:                           # data의 맨 앞이 ')'일 경우
            if is_empty():              # 만약 stack이 비어있다면
                return False            # 괄호쌍이 맞지 않다는 뜻이므로 False 반환
            elif stack[-1] == '(':      # 만약 stack의 마지막 값이 '('이라면 쌍이 맞으므로
                data = data[1:]         # data의 맨 앞을 제외하고 슬라이싱 한 뒤
                pop()                   # stack의 마지막 값을 pop

    if is_empty():                      # 정상적으로 모두 while문이 돌았을 때 stack이 비어있다면
        return True                     # True를 반환
    else:                               # while문이 모두 돌았음에도 stack이 남아있다면 괄호쌍이 맞지 않는다는 뜻이므로
        return False                    # False 반환



import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
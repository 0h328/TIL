def push(item):

    stack.append(item)

def pop():

    if stack:
        return stack.pop()
    return

def is_empty():

    if not stack:
        return True
    else:
        return False

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용

    for i in data:                  # 입력받은 문자열을 돌면서
        if i == '(':                # 문자가 '(' 일 경우,
            push('(')               # stack에 '(' append
        elif i == ')':              # 문자가 ')' 일 경우,
            if stack[-1] == '(':    # stack의 마지막 index가 '('라면,
                pop()               # pop을 해주고
            # if is_empty():
            #     return False
            # pop()
            else:                   # '('가 아니라면,
                return False        # False를 반환해준다.

    if is_empty():                  # stack이 비어있으면,
        return True                 # True를 반환해주고
    else:                           # 아니라면,
        return False                # False를 반환해준다.

import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
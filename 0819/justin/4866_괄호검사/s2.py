class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

def solve(word):
    match = {               # 닫는 괄호 먼저 세팅
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = Stack()
    for char in word:
        if char in '({[':     # 여는 괄호를 만나면
            stack.push(char)  # 바로 push
        elif char in match:   # 닫는 괄호를 만났을 때
            if stack.is_empty(): # 스택이 비어 있으면 올바르지 않은 수식
                return False     # 여는 괄호가 무조건 스택이 있어야 pop 가능
            else:                # 스택이 비어있지 않으면
                pop_char = stack.pop()      # 마지막에 들어간 요소를 스택에서 꺼내서
                if pop_char != match[char]: # 쌍을 이루지 않으면 올바르지 않은 수식
                    return False
    return stack.is_empty()                 # 스택이 있으면 짝을 찾은 것이고 비어있지 않으면 찾지 못한 것

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    code = input()
    if solve(code):
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
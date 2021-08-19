import sys
sys.stdin = open('input.txt')

# s2.py
# 배열 (고정크기)

SIZE = 5             # 크기가 5인 배열을 생성하기 위한 변수 초기화
top = -1             # top의 기본값
stack = [0] * SIZE   # 5 크기의 배열 생성

def push(item):
    global top, stack
    top += 1
    if top == SIZE:
        print('Stack is Full!')
        top -= 1
        return
    stack[top] = item

def pop():
    global top, stack
    if top == -1:
        print('Stack is Empty!')
        return
    top -= 1
    return stack.pop(top + 1)

print(stack)      # [0, 0, 0, 0, 0]
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)           # Stack is Full!
print(stack)      # [1, 2, 3, 4, 5]

item = pop()
print(item) # 5
item = pop()
print(item) # 4
item = pop()
print(item) # 3
item = pop()
print(item) # 2
item = pop()
print(item) # 1
item = pop()
print(item) # Stack is Empty!
"""
연습 문제1. 고정 배열로 Stack 구현
"""

SIZE = 5             # 크기가 5인 배열을 생성하기 위한 변수 초기화
top = -1             # top의 기본값
stack = [0] * SIZE   # 5 크기의 배열 생성

def push(item):
    global top, stack
    if top >= SIZE - 1:         # top이 다 찬 경우 (SIZE-1 -> 마지막 인덱스)
        print('Stack is Full!')
        return                  # 함수를 종료하기 위함
    else:                       # 아직 남아있는 경우
        top += 1                # top을 1 증가
        stack[top] = item       # top이 가리키는 자리에 item 추가

def pop():
    global top, stack
    if top == -1:               # top이 -1이면(stack이 비어있으면)
        print('Stack is Empty!')
        return                  # 함수 종료
    else:                       # 0이 아니면
        result = stack[top]     # stack의 top이 가리키는 위치에 있는 값을 result에 넣고
        top -= 1                # top 크기를 1개 감소 시키고
        return result           # 그 값을 반환

print(stack)      # [0, 0, 0, 0, 0]
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
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
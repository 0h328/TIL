# 08/18 Stack 1

| No.  | Title             | Directory               | PPT 번호 |
| ---- | ----------------- | ----------------------- | ---- |
|  | Stack 구현 | `연습문제_1` | 9 |
|  | 괄호매칭 | `연습문제_2` | 14 |
| 5432 | 쇠막대기 자르기 | `5432_쇠막대기자르기` | |
| 2005 | 파스칼의 삼각형(HW) | `2005_파스칼의삼각형` | |



## 연습문제 1

```python
# 리스트 (가변크기)

stack = []

def push(item):
    pass

def pop():
    pass

print(stack) # []
push(1)
push(2)
push(3)
print(stack) # [1, 2, 3]

print('---------')
# 가장 뒤(위)부터 pop
print(pop()) # 3
print(pop()) # 2
print(pop()) # 1

```

```python
s2-1.py
# 배열 (고정크기)

SIZE = 5             # 크기가 5인 배열을 생성하기 위한 변수 초기화
top = -1             # top의 기본값
stack = [0] * SIZE   # 5 크기의 배열 생성

def push(item):
    global top, stack
    pass

def pop():
    global top, stack
    pass

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
```

```python
s2.py
# 클래스로 stack 구현

class Stack:
    def __init__(self):                          # 생성자 메서드
        pass

    def is_empty(self):                          # stack이 비어있는지 체크하는 메서드
        pass

    def push(self, item):                        # stack에 push하는 메서드
        pass

    def pop(self):                              # stack에서 pop하는 메서드 (없는 경우 None)
        pass

    def __str__(self):                          # stack 출력
        result = '\n-----'
        for d in self.data:
            result = '\n| {} |'.format(d) + result
        return result


stack = Stack()          # stack 인스턴스 생성
print(stack.is_empty())  # True

stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
"""
| 3 |
| 2 |
| 1 |
"""
print(stack.is_empty())  # False

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())  # True
print(stack)             # None
```

> python의 `global` keyword

https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value

https://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python

```python
# 동작 - 참조 가능
x = 10
def foo_bar():
    y = 2
    return x + y

print(foo_bar()) # 12

# 에러 - 변경 불가능
x = 10
def foo_bar():
    y = 2
    x += 2
    return x + y

print(foo_bar()) # UnboundLocalError: local variable 'x' referenced before assignment

# 해결 - 전역 변수 변경
x = 10
def foo_bar():
    global x
    y = 2
    x += 2
    return x + y

print(foo_bar()) # UnboundLocalError: local variable 'x' referenced before assignment
```





## 연습문제 2

```python
# input.txt

()()((()))
((()((((()()((()())((())))))
```

```python
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
    pass

def pop():
    pass

def is_empty():
    pass

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    pass

import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
```
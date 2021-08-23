# s2.py
# 클래스로 stack 구현

class Stack:
    def __init__(self):                          # 생성자 메서드
        self.data = []

    def is_empty(self):                          # stack이 비어있는지 체크하는 메서드
        if len(self.data) == 0:
            return True
        return False

    def push(self, item):                        # stack에 push하는 메서드
        self.data.append(item)

    def pop(self):                              # stack에서 pop하는 메서드 (없는 경우 None)
        # 확인->stack에 요소가 존재하는가?
        if self.is_empty():
            return stack.pop()


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
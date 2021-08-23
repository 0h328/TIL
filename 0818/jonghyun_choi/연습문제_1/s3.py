# s2.py
# 클래스로 stack 구현

class Stack:
    def __init__(self):                          # 생성자 메서드
        self.data = []

    def is_empty(self):                          # stack이 비어있는지 체크하는 메서드
        return len(self.data) == 0

    def push(self, item):                        # stack에 push하는 메서드
        self.data.append(item)
        return self.data

    def pop(self):                              # stack에서 pop하는 메서드 (없는 경우 None)
        ans = self.data.pop()
        return ans

    def __str__(self):                          # stack 출력
        result = '\n-----'
        if self.data:
            for d in self.data:
                result = '\n| {} |'.format(d) + result
            return result
        else:
            return 'None'

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
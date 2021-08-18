class Stack:
    def __init__(self):                          # 생성자 메서드
        self.len = 0
        self.data = []

    def is_empty(self):                          # stack이 비어있는지 체크하는 메서드
        if self.len == 0:
            return True
        else:
            return False

    def push(self, item):                        # stack에 push하는 메서드
        self.len += 1
        self.data.append(item)

    def pop(self):                              # stack에서 pop하는 메서드 (없는 경우 None)
        if self.len == 0:
            return None
        else:
            self.len -= 1
            return self.data.pop()

    def __str__(self):                          # stack 출력
        if self.len:
            result = '\n-----'
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

print(stack.pop())       # 3
print(stack.pop())       # 2
print(stack.pop())       # 1
print(stack.is_empty())  # True
print(stack)             # None
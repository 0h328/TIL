"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # self.items.insert(0, item)
        self.items.append(item)

    def dequeue(self):
        # return self.items.pop(-1)
        # return self.items.pop()
        return self.items.pop(0)

    def size(self):
        return len(self.items)

Q = Queue()

print(Q.is_empty())     # True
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.items)           # [3, 2, 1]
print(Q.size())          # 3
print(Q.is_empty())      # False
print(Q.dequeue())       # 1
print(Q.items)           # [3, 2]
print(Q.dequeue())       # 2
print(Q.items)           # [3]
print(Q.dequeue())       # 3
print(Q.items)           # []
print(Q.size())          # 0
print(Q.is_empty())      # True
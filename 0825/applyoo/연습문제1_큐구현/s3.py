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
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# 1. Queue 인스턴스 생성
Q = Queue()

# 2. Queue가 비었는지 확인
print(Q.is_empty())

# 3. 1, 2, 3 원소를 Queue 삽입
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(Q.items)
print(Q.size())

# 5. Queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.is_empty())
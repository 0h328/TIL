"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""


class Queue:
    def __init__(self):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.items = []

    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return not bool(self.items)

    def enqueue(self,item):
        """
        Queue에 원소 삽입
        """
        self.items.append(item)

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        return self.items.pop(0)

    def size(self):
        """
        Queue의 길이 반환
        """
        return len(self.items)

# 1. Queue 인스턴스 생성
q=Queue()
print(q.is_empty())
# 2. Queue가 비었는지 확인

# 3. 1, 2, 3 원소를 Queue 삽입
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(q.items)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
# 5. Queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

class Queue:
    def __init__(self, n):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        self.Q = [0] * n
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        return self.front == self.rear

    def enqueue(self, item):
        """
        Queue에 원소 삽입
        """
        self.rear += 1
        self.Q[self.rear] = item

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        if self.is_empty():
            print("Queue_Empty")
        else:
            self.front += 1
            return self.Q[self.front]

    def size(self):
        """
        Queue의 길이 반환
        """
        return self.rear - self.front


#1. Queue 인스턴스 생성
Q = Queue(3)

#2. Queue가 비었는지 확인
print(Q.is_empty())

#3. 1, 2, 3 원소를 Queue 삽입
for i in range(1, 4):
    Q.enqueue(i)

#4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(Q.Q)
print(Q.size())
print(Q.is_empty())
#5. Queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print('dequeue', Q.dequeue())
print('size', Q.size())
print('is_empty', Q.is_empty())
print('dequeue', Q.dequeue())
print('size', Q.size())
print('is_empty', Q.is_empty())
print('dequeue', Q.dequeue())
print('size', Q.size())
print('is_empty', Q.is_empty())
print('dequeue', Q.dequeue())
print('size', Q.size())
print('is_empty', Q.is_empty())

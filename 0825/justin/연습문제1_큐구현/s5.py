# 참고 -> 원형큐 클래스 구현

class Queue:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = 0   # 원형 Queue의 초기 공백 상태를 0으로 초기화
        # 원형큐에서 가장 앞을 비워두는 이유 것은 공백 상태의 큐와 포화 상태의 큐를 용이하게 파악하기 위함
        # size보다 1개 더 큰 크기로 배열 초기화 -> None으로 초기화
        self.items = [None for _ in range(size + 1)]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        # 모듈로 연산 활용
        return self.front == (self.rear + 1) % (self.size + 1)

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full!')
        else:
            # rear 값을 조정하여 삽입 할 자리를 준비하고
            self.rear = (self.rear + 1) % (self.size + 1)
            # 해당 위치에 item 삽입
            self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            # front 값을 조정하여 삭제 할 자리를 준비하고
            self.front = (self.front + 1) % (self.size + 1)
            # 해당 위치의 item 반환
            return self.items[self.front]

    def show(self):
        start = (self.front + 1) % (self.size + 1)
        print('<<', end=' ')
        if start < self.rear:
            for index in range(start, self.rear + 1):
                print(self.items[index], end=' ')
        else:
            for i in range(start, self.size + 1):
                if self.items[i]:
                    print(self.items[i], end=' ')

            for i in range(self.rear + 1):
                print(self.items[i], end=' ')

        print('<<')

# queue의 사이즈를 지정
q = Queue(4)
print(q.items) # [None, None, None, None, None]
print('----------------------------------')

# 3개의 데이터 삽입
print(q.is_empty()) # True
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.is_empty()) # False
q.show() # << 1 2 3 <<
print('----------------------------------')


# 3개 데이터 제거
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty()) # True
q.show() # << None 1 2 3 <<
print('----------------------------------')


q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.show() #
print(q.is_empty()) # False
print(q.is_full()) # False
print('----------------------------------')


q.enqueue(7)
q.show()
print(q.is_full()) # True
q.enqueue(8) # Queue is full!
q.show() # << 4 5 6 7 <<
print('----------------------------------')


print(q.dequeue()) # 4
print(q.dequeue()) # 5
q.show() # << 6 7 <<
print('----------------------------------')
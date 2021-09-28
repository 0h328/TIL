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
        return self.items == []

    def enqueue(self):
        """
        Queue에 원소 삽입
        """
        self.items.append(item)

    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        return sel.items.pop(0)

    def size(self):
        """
        Queue의 길이 반환
        """
        return len(self.items)


#1. Queue 인스턴스 생성
Q = Queue()
#2. Queue가 비었는지 확인
print(Q.is_empty())
#3. 1, 2, 3 원소를 Queue 삽입
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.is_empty())
#4. 원소가 정상적으로 삽입되었는지/ 사이즈/ 비었는지 여부 확인
print(Q.items)
print(Q.size())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.is_empty())
#5. Queue에서 원소 삭제 후 반환 & 원소 확인/ 사이즈 확인
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))

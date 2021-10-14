"""
문제3. 고정 배열 크기의 Queue 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""
SIZE = 4
Q = [0] * SIZE
front, rear = -1, -1

def is_full():
    #Queue 포화 확인
    return rear == len(Q) - 1

def is_empty():
    #Queue 공백 확인
    return front == rear

def enque(item):
    global rear
    if is_full():
        print('Queue is full!!')
    else:
        rear += 1
        Q[rear] = item
def dequeue():
    global front
    if is_empty():
        print('Queue is empty!')
    else:
        front += 1
        return Q.pop(0)

def Qpeek():
    if is_empty():
        print('Queue is empty!')
    else:
        return Q[front+1]
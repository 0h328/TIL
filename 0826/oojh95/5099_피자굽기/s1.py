import sys
sys.stdin = open('input.txt')
def is_full():
    """
    Queue가 포화상태인지 확인
    """
    return (rear + 1) % len(Q) == front

# isEmpty
def is_empty():
    """
    Queue가 공백상태인지 확인
    """
    return front == rear


# enQueue
def enqueue(item):

    """
    Queue의 뒤쪽(rear 다음)에 원소를 삽입
    - rear를 뒤쪽으로 옮기고 (rear + 1)그 자리에 원소를 삽입
    """
    global rear

    if is_full():
        print('Queue is full!')
    else:

        rear = (rear+1) % len(Q)
        Q[rear] = item



# deQueue
def dequeue():
    """
    Queue의 앞쪽(front)에서 원소를 삭제하고 반환
    - front를 뒤쪽으로 옮기고(front + 1) 그 자리에 있는 원소를 반환하며 삭제
    """
    global front
    if is_empty():
        print('Queue is empty!')
    else:
        front = (front+1) % len(Q)
        return Q[front]


# Qpeek
def Qpeek():
    """
    Queue의 앞쪽(front)의 한 자리뒤(front+1)에서 원소를 삭제없이 반환
    - front의 값을 단순하게 증가시켜 가져온다. (큐의 첫 번째 원소 반환)
    - 이때 중요한 것은 dequeue와 다르게 front의 값 자체를 '변경'하지 않는다는 점
     - front += 1은  front + 1과 다름
    """
    if is_empty():
        print('Queue is empty!')
    else:
        return Q[front]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    Q = [0] * N
    # 초기 상태의 표현
    front, rear = -1, -1
    i = 0
    while i < M:
        if is_full():
            tmp = (dequeue()//2)
            if tmp == 0:
                enqueue(Ci[i])
                i += 1
            else:
                enqueue(tmp)
                dequeue()
        if not is_full():
            enqueue(Ci[i])
            i += 1


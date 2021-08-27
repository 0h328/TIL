import sys
sys.stdin = open('input.txt')


def is_full():

    return rear == len(Q) - 1

def is_empty():

    return front == rear

def enqueue(item):

    global rear

    if is_full():
        print('Queue is full!')
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

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    Q = [0] * N
    front, rear = -1, -1

    for i in range(M):
        if is_full():
            tmp = dequeue() // 2
            if tmp == 0:
                enqueue(Ci[i])
            else:
                enqueue(tmp)
        else:
            enqueue(Ci[i])



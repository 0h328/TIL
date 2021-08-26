def deQueue():
    global front
    front += 1
    front %= len(Q)
    ans = Q[front]
    Q[front] = 0
    return ans

def enQueue(item):
    global rear
    rear += 1
    rear %= len(Q)
    Q[rear] = item

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    front = 0
    rear = N
    Q = [0] + nums
    # print(Q)

    for i in range(M):
        num = deQueue()
        enQueue(num)

    # print(front, rear, Q)

    front += 1
    front %= len(Q)

    print('#{} {}'.format(tc, Q[front]))
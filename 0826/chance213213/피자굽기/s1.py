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
    #N: 화덕에 들어갈 수 있는 피자 개수
    #M: 구워야 하는 피자 개수

    cheeze = list(map(int, input().split()))
    #치즈 양 리스트

    Q = [0] * (N+1) #화덕이라고 생각
    enable = [0] * M # [0 0 0 0 0]
    front = 0
    rear = N
    #
    # for idx in range(M):
    #     if Q.count(0)>=2 and enable[idx] ==0:
    #         enQueue(cheeze[idx])
    #         enable[idx] == 1
    #일단 화덕에 한번 돌리고 다 된거 빼내는 거 까지
    for idx in range(N):
        enQueue(cheeze[idx]) #화덕에 피자 한세트 넣음
    print(Q)
    for idx in range(N):
        c = deQueue() // 2
        if c == 0:
            deQueue()
            enQueue(cheeze[3])
        else:
            enQueue(c)




    print()
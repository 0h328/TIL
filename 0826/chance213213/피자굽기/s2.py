#그냥 피자 리스트 다 받아와서, 거기서 front, rear로만 화덕 써먹기
# 다 구워지면 pop해서 내보내면 됨
def deQueue():
    global front
    front += 1
    front %= N
    ans = cheeze[front]
    cheeze[front] = 0
    return ans

def enQueue(item):
    global rear
    rear += 1
    rear %= N
    cheeze[rear] = item

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    #N: 화덕에 들어갈 수 있는 피자 개수
    #M: 구워야 하는 피자 개수

    cheeze = list(map(int, input().split()))
    #치즈 양 리스트
    #눈으로 구분 용
    print(cheeze)
    enable = [0] * M  # [0 0 0 0 0]

    front = -1
    rear = N-1
    #%하는 수는 N으로 하면 되겠네

    while cheeze.count(0) < 2:
        C = deQueue()
        C //= 2
        if C == 0 and len(cheeze) > N:
            cheeze.pop(front)

            front -= 1
        elif C==0 and len(cheeze) <= N:
            deQueue()
        else:
            enQueue(C)
            print(cheeze)

    print(cheeze)
    print()

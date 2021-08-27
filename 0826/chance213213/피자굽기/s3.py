# 그냥 피자 리스트 다 받아와서, 거기서 front, rear로만 화덕 써먹기
# 다 구워지면 pop해서 내보내면 됨
def deQueue():
    global front
    front += 1
    front %= N
    ans = pizzas[front]

    return ans


def enQueue(item):
    global rear
    rear += 1
    rear %= N
    pizzas[rear][1] = item


import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N: 화덕에 들어갈 수 있는 피자 개수
    # M: 구워야 하는 피자 개수

    cheeze = list(map(int, input().split()))
    # 치즈 양 리스트
    # 눈으로 구분 용
    # print(cheeze)
    enable = [0] * M  # [0 0 0 0 0]

    front = -1
    rear = N - 1
    # %하는 수는 N으로 하면 되겠네
    pizzas = []
    for pizza in enumerate(cheeze, start=1):
        pizza = list(pizza)
        pizzas.append(pizza)
    # print(pizzas)
    # print()

    evt = sum(pizzas, [])

    while evt.count(0) < N-1:
        C = deQueue()
        C[1] //= 2
        if C[1] == 0 and len(pizzas) > N:
            pizzas.pop(front)

            front -= 1
        elif C[1] == 0 and len(pizzas) <= N:
            deQueue()
        else:
            enQueue(C[1])
        evt = sum(pizzas, [])


    # print(pizzas)
    # print('*')
    for pizza in pizzas:
        if pizza[1]:
            ans = pizza[0]
            break
    print('#{} {}'.format(tc, ans))

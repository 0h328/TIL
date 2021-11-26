import sys
sys.stdin = open('input.txt')

from collections import deque
for T in range(int(input())):
    N, M = map(int, input().split())
    # 화덕의 크기 N
    pizza = tuple(enumerate(map(int, input().split())))

    q = deque([])

    for i in range(N):
        q.append(pizza[i])
    idx = N

    while len(q) != 1:
        if len(q)<N and idx < M:
            q.append(pizza[idx])
            idx+=1

        pizza_number, this_pizza = q.popleft()
        this_pizza//=2
        if this_pizza:
            q.append((pizza_number, this_pizza))

    result, _ = q.popleft()
    print('#{} {}'.format((T+1), result+1))


#1 4
#2 8
#3 6

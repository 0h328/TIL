import sys
sys.stdin = open('input.txt')

T = int(input())
tc = 1
while tc <= T:

    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    # print(Ci)

    index_q = [0] * N
    cheese_q = [0] * N

    pizza_idx = 0
    fire_pit_idx = 0
    while True:
        # print(cheese_q)
        # print(fire_pit_idx, end=' ')
        # print(pizza_idx)

        cheese_q[fire_pit_idx] //= 2
        rem_cheese = cheese_q[fire_pit_idx]

        if rem_cheese == 0:
            if pizza_idx < M:
                cheese_q[fire_pit_idx] = Ci[pizza_idx]
                index_q[fire_pit_idx] = pizza_idx
                pizza_idx += 1
            else:
                cheese_q[fire_pit_idx] = 0

        if not any(cheese_q):      # 전부 다 0이면
            ans = index_q[fire_pit_idx] + 1
            break

        fire_pit_idx = (fire_pit_idx + 1) % N

        # print(cheese_q)

    # cheese_q[0] = Ci[0]
    # cheese_q[1] = Ci[1]
    # cheese_q[2] = Ci[2]
    # cheese_q[0] = Ci[0] // 2
    # cheese_q[1] = Ci[1] // 2
    # cheese_q[2] = Ci[2] // 2
    # if cheese_q[0]

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1

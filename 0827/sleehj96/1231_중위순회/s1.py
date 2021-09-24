import sys
sys.stdin = open('input.txt')

def in_order(node):
    if node:
        in_order(G[node][1])
        chars.append(G[node][0])
        in_order(G[node][2])


T = 10
tc = 1
while tc <= T:
    N = int(input())
    G = [['', 0, 0] for _ in range(N+1)]    # [V, left, right]

    for _ in range(N):
        input_list = list(input().split())
        p = int(input_list[0])
        G[p][0] = input_list[1]

        list_len = len(input_list)

        if list_len >= 3:
            G[p][1] = int(input_list[2])

            if list_len == 4:
                G[p][2] = int(input_list[3])

    chars = []
    in_order(1)

    print('#{} '.format(tc), *chars, sep='')
    # break
    tc += 1

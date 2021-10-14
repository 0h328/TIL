import sys
sys.stdin = open('input.txt')

def MST():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        for i in range(V + 1):
            if not visited[i] and update[i] < min_value:
                min_idx = i
                min_value = update[i]
        visited[min_idx] = 1
        for i in range(V + 1):
            if not visited[i] and data[min_idx][i] < update[i]:
                update[i] = data[min_idx][i]
    return sum(update)


T = int(input())

for case in range(T):
    V, E = map(int, input().split())
    data = [[987654321] * (V + 1) for _ in range(V + 1)]
    update = [987654321] * (V + 1)
    update[0] = 0
    visited = [0] * (V + 1)
    for _ in range(E):
        d1, d2, cost = map(int, input().split())
        data[d1][d2] = cost
        data[d2][d1] = cost
    print('#{} {}'.format(case + 1, MST()))



import sys
sys.stdin = open('input.txt')

T = int(input())

def find_min():
    for _ in range(V):
        #min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and value_list[i] < min_value:
                min_idx = i
                min_value = value_list[i]
        visited[min_idx] = 1

        for i in range(V+1):
            if not visited[i] and G[min_idx][i] < value_list[i]:
                value_list[i] = G[min_idx][i]
    return sum(value_list)

for tc in range(1,T+1):
    V,E = map(int,input().split())
    G = [[987654321 for _ in range(V + 1)] for _ in range(V + 1)]
    value_list = [987654321] * (V+1)
    value_list[0] = 0
    visited = [0] * (V + 1)

    for i in range(E):
        start, end, W = map(int, input().split())
        G[start][end] = W
        G[end][start] = W

    ans = find_min()
    print('#{} {}'.format(tc,ans))
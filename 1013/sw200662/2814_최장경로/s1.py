import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Num_list = [[] for _ in range(N + 1)]
    ans = 0
    for _ in range(M):
        X, Y = map(int, input().split())
        Num_list[X].append(Y)
        Num_list[Y].append(X)

    for i in range(1, len(Num_list)):
        visited_list = [0] * (N + 1)
        visited_list[i] = 1
        que = []
        for k in Num_list[i]:
            que.append(k)
            visited_list[k] = 1
        cnt = 1
        while len(que) != 0:
            cnt +=1
            temp2 = que.pop()
            for z in Num_list[temp2]:
                if visited_list[z] == 0:
                    que.append(z)
                    visited_list[z] = 1
        if ans < cnt:
            ans = cnt

    print('#{} {}'.format(tc, ans))

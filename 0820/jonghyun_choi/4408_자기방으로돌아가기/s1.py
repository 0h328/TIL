import sys
sys.stdin = open('input.txt')

T = int(input())


for case in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        A, B = map(int,input().split())
        if A < B:
            data.append((A, B))
        else:
            data.append((B, A))
    sort_data = sorted(data, key=lambda x:(x[0],x[1]))


    cnt = 0
    val = 0
    while val != N:
        s = []
        cnt += 1
        for i, j in sort_data:
            if len(s) == 0:
                s.append((i, j))
            if s[-1][1] % 2:
                if i > s[-1][1] + 1:
                    s.append((i, j))
            else:
                if i > s[-1][1]:
                    s.append((i, j))
        sort_data = [i for i in sort_data if i not in s]
        val += len(s)

    print('#{} {}'.format(case + 1, cnt))




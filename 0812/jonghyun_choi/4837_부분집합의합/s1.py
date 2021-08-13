import sys

sys.stdin = open('input.txt')

T = int(input())

for Case in range(T):
    N, K = map(int, input().split())

    num = list(range(1, 13))
    s = len(num)
    cnt = 0
    for i in range(1 << s):
        n_list = []
        for j in range(s):
            if i & (1 << j):
                n_list.append(num[j])
        if len(n_list) == N:
            if sum(n_list) == K:
                cnt += 1
    print('#{} {}'.format(Case + 1, cnt))

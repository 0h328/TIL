import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    A = [num for num in range(1, 13)]

    res = []
    for i in range(1, 1 << len(A)):
        temp = []
        for j in range(len(A)):
            if i & (1 << j):
                temp.append(A[j])
            if len(temp) > N or sum(temp) > K:
                break
        else:
            if len(temp) == N and sum(temp) == K:
                res.append(temp)

    print('#{} {}'.format(t, len(res)))
import sys

sys.stdin = open('input.txt')

T = int(input())


def find_min(a, b):
    global min
    if a == N:
        if b < min:
            min = b
        return
    if b > min:
        return
    for k in range(N):
        if check[k] == 0:
            check[k] = 1
            find_min(a + 1, b + Nums[a][k])
            check[k] = 0


for i in range(T):
    N = int(input())
    Nums = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min = 55555
    find_min(0, 0)
    print('#{} {}'.format(i+1,min))

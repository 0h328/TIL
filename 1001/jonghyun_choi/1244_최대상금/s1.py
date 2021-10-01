import sys
sys.stdin = open('input.txt')

C = int(input())


def recursive(n):
    global ans
    if n == 0:
        if ans <= int(''.join(data)):
            ans = int(''.join(data))
        return

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            data[i], data[j] = data[j], data[i]
            temp = ''.join(data)
            if visited.get((n - 1, temp), 1):
                visited[(n - 1, temp)] = 0
                recursive(n - 1)

            data[i], data[j] = data[j], data[i]



for case in range(C):
    N, M = map(int, input().split())
    data = list(str(N))
    ans = 0
    visited = {}
    recursive(M)
    print('#{} {}'.format(case + 1, ans))
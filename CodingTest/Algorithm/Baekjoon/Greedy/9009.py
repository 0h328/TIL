import sys
sys.stdin = open('input.txt')

def solution(n):
    fibo = [0, 1]
    res = []

    for i in range(2, 45):
        fibo.append(fibo[i - 2] + fibo[i - 1])

    for i in range(len(fibo) - 1, 0, -1):
        if fibo[i] <= n:
            n -= fibo[i]
            res.append(fibo[i])

    res.sort()

    return ' '.join(map(str, res))

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(solution(n))


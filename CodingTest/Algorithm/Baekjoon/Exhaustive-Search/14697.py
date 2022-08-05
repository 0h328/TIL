import sys
sys.stdin = open('input.txt')

def sol():
    A, B, C, N = map(int, input().split())

    if N % A == 0 or N % B == 0 or N % C == 0:
        return 1

    cur = 0
    for i in range(N//A + 1):
        cur = A*i - B
        for j in range(N//B + 1):
            cur += B
            if cur > N:
                break
            if (N - cur) % C == 0:
                return 1
    return 0

print(sol())
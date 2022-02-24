import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    a, b = A, B

    while A != 0:
        B = B % A
        A, B = B, A

    print(a * b // B)

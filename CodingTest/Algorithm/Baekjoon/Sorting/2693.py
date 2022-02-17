import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    print(A[2])
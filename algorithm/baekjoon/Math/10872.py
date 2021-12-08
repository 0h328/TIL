import sys
sys.stdin = open('input.txt')

def fact(N):
    if N <= 1:
        return 1

    return N * fact(N-1)

print(fact(int(input())))
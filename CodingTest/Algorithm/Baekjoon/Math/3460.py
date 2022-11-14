import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = bin(int(input()))[2:]
    for idx, val in enumerate(n[::-1]):
        if val == '1':
            print(idx, end=' ')
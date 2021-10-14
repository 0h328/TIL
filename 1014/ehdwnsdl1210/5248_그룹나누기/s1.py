def make_set(x):
    p[x] = x

def find_set(x):
????????????????


def union(x, y):
    p[find_set(y)] = find_set(x)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))

    p = [0] * (N + 1)
    for i in range(N + 1):
        make_set(i)
    # print(p)

    for i in range(len(number)//2):
        union([number[2*i]], [number[2*i + 1]])
    print(p)





#1 3
#2 2
#3 3
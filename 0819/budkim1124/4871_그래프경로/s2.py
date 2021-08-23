def function(start):
    if start == end:
        return 1
    for path in tmp:
        if path[0] == start:
            start = path[1]
            function(start)

import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(T):
    V, E = map(int, input().split())
    tmp = []

    for _ in range(E):
        t = list(map(int, input().split()))
        tmp.append(t)
    start, end = map(int, input().split())

    print(function(start))



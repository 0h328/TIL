import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0

    V, E = map(int, input().split())

    graph = [tuple(map(int, input().split())) for _ in range(E)]
    graph.sort(key=lambda i : i[2])

    included = set()

    for a, b, w in graph:
        if a not in included or b not in included:
            included.add(a)
            included.add(b)
            result+=w

    print('#{} {}'.format((T+1), result))

#1 2
#2 13
#3 22
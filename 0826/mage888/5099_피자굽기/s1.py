import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    q = []
    for i in range(M):
        q.append([i+1, data[i]])
        if len(q) == 5:



    while len(q) != 1:
        q.append(q.pop(0))
        q[len(q)-1][1] //= 2

        if q[len(q)-1][1] == 0:
            q.pop()

    print(q[0][0])

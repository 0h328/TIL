import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())
    visited = [0]* 5001
    for i in range(N):
        A, B = map(int, input().split())
        v_range = range(A,B+1)
        for j in v_range:
            visited[j] += 1

    P = int(input())
    res = []
    for stop in range(P):
        C = int(input())
        res.append(visited[C])

    print('#{} {}'.format(case + 1, ' '.join(map(str,res))))

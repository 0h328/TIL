import sys
sys.stdin = open('input.txt')


def search(n):
    global cnt
    cnt += 1

    for a in node[n]:
        search(a)


T = int(input())
for test in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    node = [[] for _ in range(E+2)]
    cnt = 0

    for i in range(E):
        node[arr[i*2]].append(arr[i*2+1])

    search(N)
    print('#{} {}'.format(test+1, cnt))

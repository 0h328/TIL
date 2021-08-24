import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    a_l = []

    for _ in range(5):
        a_l.append(max(a))
        a.pop(a.index(max(a)))
        a_l.append(min(a))
        a.pop(a.index(min(a)))

    print('#{}'.format(tc), end=' ')
    print(*a_l)
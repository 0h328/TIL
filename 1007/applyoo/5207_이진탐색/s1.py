import sys
sys.stdin = open('input.txt')


def binary_search(l, r, x):
    flag = 'r' if A[(r+l)//2] > x else 'l'
    while r >= l:
        m = (r+l) // 2
        if A[m] > x and flag == 'r':
            r = m - 1
            flag = 'l'
        elif A[m] < x and flag == 'l':
            l = m + 1
            flag = 'r'
        elif A[m] == x:
            return 1
        else:
            return 0
    return 0


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A, B = sorted(list(map(int, input().split()))), list(map(int, input().split()))

    res = 0
    for b in B:
        res += binary_search(0, len(A)-1, b)
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')

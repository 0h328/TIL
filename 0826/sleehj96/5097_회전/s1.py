import sys
sys.stdin = open('input.txt')

T = int(input())
tc = 1
while tc <= T:

    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    move = M % N
    ans = q[move]

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1

import sys
from itertools import permutations
sys.stdin = open('input.txt')


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321

    for case in permutations([n for n in range(1, N)]):
        t_ans = 0
        start_point = 0

        for step in case:
            t_ans += G[start_point][step]
            start_point = step
        t_ans += G[start_point][0]

        if ans > t_ans:
            ans = t_ans

    print('#{0} {1}'.format(tc+1, ans))
    # break

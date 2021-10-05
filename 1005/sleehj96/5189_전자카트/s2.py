import sys
sys.stdin = open('input.txt')


def perm(n, depth):

    if depth == N-1:
        cases.append(tuple(num_list))
        return

    for i in range(n, N-1):
        num_list[n], num_list[i] = num_list[i], num_list[n]
        perm(n+1, depth+1)
        num_list[n], num_list[i] = num_list[i], num_list[n]


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321

    cases = []
    num_list = [n for n in range(1, N)]
    perm(0, 0)     # depth, start_idx

    for case in cases:
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

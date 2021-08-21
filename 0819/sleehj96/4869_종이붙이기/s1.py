import sys


def how_many_case(n):
    if n == 1:
        return 1
    else:
        i = 2
        while i <= n:
            paper_patch_list.append(2 * paper_patch_list[i-2] + paper_patch_list[i-1])
            i += 1
        return paper_patch_list[n]

sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:
    N = int(input()) // 10

    ans = 0

    paper_patch_list = [1, 1]

    ans = how_many_case(N)

    print('#{0} {1}'.format(test_case, ans))
    # break
    test_case += 1

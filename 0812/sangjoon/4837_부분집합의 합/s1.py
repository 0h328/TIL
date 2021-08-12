import pathlib, sys

# from itertools import combinations

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):

    n, k = map(int, input().split())

    lst = [i for i in range(1, 13)]
    L = len(lst)

    ans = 0

    for i in range(1, 1 << L):
        subset = []
        for j in range(L):
            if i & (1 << j):
                subset.append(lst[j])

        if len(subset) == n and sum(subset) == k:
            ans += 1

    # n, k = map(int, input().split())
    # lst = [i for i in range(1, 12)]
    # comb_lst = list(combinations(lst, n))
    # ans = 0

    # for comb in comb_lst:
    #     if sum(comb) == k:
    #         ans += 1

    print("#{} {}".format(test, ans))
import pathlib, sys
from itertools import combinations

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):

    n, k = map(int, input().split())
    lst = [i for i in range(1, 12)]
    comb_lst = list(combinations(lst, n))
    ans = 0

    for comb in comb_lst:
        if sum(comb) == k:
            ans += 1

    print("#{} {}".format(test, ans))
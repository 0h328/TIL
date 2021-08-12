import pathlib, sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        if i % 2:
            min_idx = i
            for j in range(i, len(lst)):
                if lst[j] < lst[min_idx]:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]

        else:
            max_idx = i
            for j in range(i, len(lst)):
                if lst[j] > lst[max_idx]:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]

    print("#{}".format(test), end=" ")
    print(" ".join(map(str, lst[:10])))
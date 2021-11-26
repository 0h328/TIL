import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = 1

for test in range(1, test_case + 1):
    ans = 0
    lst = list(map(int, input().split()))
    N = len(lst)

    for i in range(1, 1 << N):
        for j in range(N):
            if i & (1 << j):
                print(lst[j], end=" ")
        print()

    print("#{} {}".format(test, ans))
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    ans = 0
    print("#{} {}".format(test, ans))
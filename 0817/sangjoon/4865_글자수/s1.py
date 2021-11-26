import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = input()
    m = input()
    ans = 0

    for alphabet in n:  # 알파벳 순회
        cnt = m.count(alphabet)
        ans = max(ans, cnt)  # 최대 알파벳 개수

    print("#{} {}".format(test, ans))
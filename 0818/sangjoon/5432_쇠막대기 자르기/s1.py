import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    lst = list(input())
    stack = []
    ans = 0

    while lst:
        e = lst.pop()

        if e == ")":
            if lst[-1] == "(":  # 레이저라면
                lst.pop()
                ans += len(stack)
            else:  # 막대기 시작
                stack.append(e)

        else:  # 막대기가 끝
            stack.pop()
            ans += 1

    print("#{} {}".format(test, ans))
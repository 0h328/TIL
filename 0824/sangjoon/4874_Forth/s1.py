def calculate_postfix(postfix: list):
    stack = []
    operator = ["+", "-", "/", "*"]
    for i in range(len(postfix)):
        l = postfix[i]
        if l == ".":  # 수식이 끝날 경우
            if len(stack) != 1 or i != len(postfix) - 1:  # 수식이 불완전하거나 "."이 중간에 나올 경우
                return "error"

            return stack.pop()

        elif l in operator:  # 연산자일 경우
            if len(stack) < 2:
                return "error"

            num1 = stack.pop()
            num2 = stack.pop()
            temp = int(eval(num2 + l + num1))
            stack.append(str(temp))

        elif l.isdigit():  # 숫자일 경우
            stack.append(l)

        else:  # 이외의 표현이 나왔을 경우
            return "error"


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    postfix = list(input().split())
    ans = calculate_postfix(postfix)
    print("#{} {}".format(test, ans))
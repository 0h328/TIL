import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def get_postfix(prefix: str):
    ans = ""
    stack = []
    for l in prefix:
        if l.isdigit():
            ans += l
        else:
            if l == "+":
                while stack:  # 우선순위가 높은 것을 pop
                    ans += stack.pop()
                stack.append(l)
            elif l == "*":  # 우선순위가 높은 연산자가 없으므로 그대로 append
                stack.append(l)

    while stack:  # 남은 연산자 추가
        ans += stack.pop()

    return ans


def calculate_postfix(postfix: str):

    stack = []
    for l in postfix:
        if l.isdigit():  # 숫자일 경우 스택에 추가
            stack.append(l)
        else:  # 연산자일 경우 스택의 두 숫자를 계산
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(str(eval(num1 + l + num2)))

    res = stack.pop()  # 마지막 남은 연산자를 스택에서 꺼냄
    return res


for test in range(1, 11):
    n = input()
    prefix = input()

    postfix = get_postfix(prefix)
    ans = calculate_postfix(postfix)
    print("#{} {}".format(test, ans))
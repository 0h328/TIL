import sys
sys.stdin = open('input.txt')

def change_experession(original):
    stack = []
    push_priority = {"+": 0, "-": 0, "*": 1, "/": 1, "[": 2, "{": 3, "(": 4}
    pop_priority = {"+": 0, "-": 0, "*": 1, "/": 1, "(": -1, "{": -2, "[": -3}
    result = ""

    for i in range(N):
        if original[i].isdigit():
            result += original[i]
        else:
            if original[i] == ")":
                while True:
                    temp = stack.pop()
                    if temp == "(":
                        break
                    result += temp
            elif original[i] == "}":
                while True:
                    temp = stack.pop()
                    if temp == "{":
                        break
                    result += temp
            elif original[i] == "]":
                while True:
                    temp = stack.pop()
                    if temp == "[":
                        break
                    result += temp
            else:
                if not stack:
                    stack.append(original[i])
                else:
                    if push_priority[original[i]] > pop_priority[stack[-1]]:
                        stack.append(original[i])
                    else:
                        while True:
                            result += stack.pop()
                            if not stack or push_priority[original[i]] > pop_priority[stack[-1]]:
                                stack.append(original[i])
                                break
    while stack:
        result += stack.pop()

    return result


def calc_expression(expression):
    stack = []

    for i in range(len(expression)):
        if expression[i].isdigit():
            stack.append(expression[i])
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if expression[i] == "+":
                stack.append(num1 + num2)
            elif expression[i] == "*":
                stack.append(num1 * num2)
            elif expression[i] == "-":
                stack.append(num1 - num2)
            elif expression[i] == "/":
                stack.append(num1 // num2)

    return stack


T = 10

for tc in range(1, T + 1):
    N = int(input())
    original = input()
    changed = change_experession(original)
    ans = calc_expression(changed)

    print("#{} {}".format(tc, *ans))

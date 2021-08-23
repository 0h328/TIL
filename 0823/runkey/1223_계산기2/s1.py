import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    data = input() # 중위 표기식
    stack = []
    num = ""
    #1. 중위 표현식 -> 후위 표현식

    for char in data:
        if char == "*":
            stack.append(char)
        elif char == "+":
            # stack.append(char)
            # 이 경우 고려해야 할 사항?
            # stack이 비어있는지 여부 판단 & stack의 가장 위 (top)가 * 연산자인지 확인
            while stack:
                num += stack.pop()
            stack.append(char)
        else:
            num += char
    while stack:
        num += stack.pop()

    #2. 후위 표현식 -> 계산

    for char in num:
        if char == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) * int(a))
        elif char == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) + int(a))
        else:
            stack.append(char)
    num = stack.pop()
    print("#{} {}".format(tc, num))
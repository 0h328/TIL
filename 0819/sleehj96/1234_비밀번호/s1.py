import sys

sys.stdin = open('input.txt')

T = 10
test_case = 1

while test_case <= T:
    N, input_str = input().split()
    stack = []

    for letter in input_str:
        if not stack:
            stack.append(letter)
        else:
            if letter != stack[-1]:
                stack.append(letter)
            else:
                stack.pop()

    pwd = ''
    for e in stack:
        pwd += e

    print('#{0} {1}'.format(test_case, pwd))
    # break
    test_case += 1

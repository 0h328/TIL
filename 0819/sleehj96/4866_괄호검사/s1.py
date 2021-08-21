import sys

sys.stdin = open('input.txt')

opening_brackets = ['(', '{', '[']
closing_brackets = [')', '}', ']']
T = int(input())
test_case = 1

while test_case <= T:
    code = input()

    ans = 0
    stack = []

    for idx in range(len(code)):

        if code[idx] in opening_brackets:    # 여는 괄호면
            stack.append(code[idx])          # 스택에 추가
        elif code[idx] in closing_brackets:  # 닫는 괄호면
            # print(stack)
            if stack:   # 스택이 채워져 있으면
                if closing_brackets.index(code[idx]) != opening_brackets.index(stack[-1]):
                    break
                else:
                    stack.pop()             # 스택에서 뽑아냄
            else:
                break
    else:   # 다 확인했는데
        if not stack:   # 스택이 비어있으면
            ans = 1     # 참

    print('#{0} {1}'.format(test_case, ans))
    # break
    test_case += 1

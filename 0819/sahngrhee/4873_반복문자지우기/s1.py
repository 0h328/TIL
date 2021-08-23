import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    C = input()
    stack = [C[0]]
    for i in range(1, len(C)):
        if len(stack) > 0:
            if C[i] != stack[-1]:
                stack.append(C[i])
            else:
                stack.pop()
        else:
            stack.append(C[i])
    ans = len(stack)

    print('#{} {}'.format(test_case, ans))



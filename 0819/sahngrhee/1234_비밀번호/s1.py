import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    n, password = input().split()
    N = int(n)
    stack = []

    for i in range(N):
        if len(stack) == 0:
            stack.append(password[i])
        else:
            if stack[len(stack)-1] == password[i]:
                stack.pop()
            else:
                stack.append(password[i])

    ans = ''.join(stack)
    print('#{} {}'.format(test_case, ans))
import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1, t+1):
    # string = input()
    # idx, cnt, total = 0, 0, 0
    # while idx < len(string):
    #     if string[idx] == '(' and string[idx+1] == ')':
    #         total += cnt
    #         idx += 2
    #         continue
    #     elif string[idx] == '(':
    #         cnt += 1
    #     else:     # )
    #         cnt -= 1
    #         total += 1
    #     idx += 1




    stack = list(input())
    top = len(stack) - 1
    total = 0
    cnt = 0
    while stack:
        x = stack.pop(top)
        top -= 1
        if x == ')' and stack[top] == '(':
            stack.pop()
            top -= 1
            total += cnt
        elif x == ')':
            cnt += 1
        else:
            cnt -= 1
            total += 1

    print('#{} {}'.format(num, total))






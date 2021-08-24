

def push(item):
    global top, stack

    stack.append(item)
    top += 1

def pop():
    global top, stack
    if top == -1:
        return
    else:
        ans = stack.pop()
        top -= 1
        return ans

def solve(nums):
    stack = []
    for num in nums:
        if num == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a+b)
        elif num == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a*b)
        else:
            stack.append(int(num))
        # print(stack, num)

    return stack.pop()


import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    top = -1
    new = []

    for chr in arr:
        if chr == '*' or chr == '+':
            if top == -1 or ord(chr) < ord(stack[top]):
                push(chr)
            elif ord(chr) >= ord(stack[top]):
                for _ in range(len(stack)):
                    if ord(chr) < ord(stack[top]):
                        break
                    new.append(pop())

                push(chr)

        else:  # type(int(chr)) == 'int':
            new.append(chr)
    else:
        for _ in range(len(stack)):
            new.append(stack.pop())

    # print('stack:{}'.format(stack))
    # print('arr:{}'.format(arr))
    # print('new:{}'.format(new))

    print('#{} {}'.format(tc, solve(new)))
    # print(len(arr), len(new))
#
# def solve(stack, chr):
#     # if bool(stack) == False: #비어 있을 때
#     if chr == '*' or chr == '+':
#             push()
#
#     else:# type(int(chr)) == 'int':
#         new.append(chr)
    #
    # else:
    #     if top != -1 and stack[top] == '+' and chr == '+':
    #         pop()
    #         push()
    #
    #     elif top != -1 and stack[top] == '+' and chr == '*':
    #         push()
    #
    #     elif top != -1 and stack[top] == '*' and chr == '+':
    #         pop()
    #         push()
    #
    #     elif top != -1 and stack[top] == '*' and chr == '*':
    #         pop()
    #         push()

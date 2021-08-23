import sys
sys.stdin = open('input2.txt')

N = int(input())
arr = list(input())
stack = []
top = -1
new = []

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




for chr in arr:
    if chr == '*' or chr == '+':
        if top == -1 or ord(chr) < ord(stack[top]):
            push(chr)
        elif ord(chr) >= ord(stack[top]):
            new.append(pop())
    else:  # type(int(chr)) == 'int':
        new.append(chr)

print('stack:{}'.format(stack))
print('new:{}'.format(new))
print('arr:{}'.format(arr))


def solve(stack, chr):
    # if bool(stack) == False: #비어 있을 때
    if chr == '*' or chr == '+':
            push()

    else:# type(int(chr)) == 'int':
        new.append(chr)
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

print(arr)
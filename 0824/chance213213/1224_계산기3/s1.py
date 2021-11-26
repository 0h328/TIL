import sys
sys.stdin = open('input.txt')
stack = []
def push(chr):
    global top, stack
    stack.append(chr)
    top += 1

def pop():
    global top, stack
    ans = stack.pop()
    top -= 1
    return ans
def solve(nums):
    global stack
    for num in nums:
        if num == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        elif num == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)
        else:
            stack.append(int(num))
        # print(stack, num)

    return stack.pop()

# def solve(nums):


for tc in range(1, 11):
    stack = []

    top = -1
    N = int(input())
    data = list(input())
    new_data = []
    for chr in data:
        if chr in ['*', '+', '(']:
            if top != -1 and stack[top] == '(':
                push(chr)
            elif top == -1 or ord(chr) < ord(stack[top]):
                push(chr)
            elif ord(chr) >= ord(stack[top]):
                for _ in range(len(stack)):
                    if stack[top] == '(':
                        break
                    if ord(chr) < ord(stack[top]):
                        break
                    new_data.append(pop())
                push(chr)
        elif chr == ')':
            for _ in range(len(stack)):
                if stack[top] == '(':
                    pop()
                    break
                new_data.append(pop())
        else:
            new_data.append(chr)
    else:
        for _ in range(len(stack)):
            new_data.append(stack.pop())
    # print(new_data)
    # print(data)

    print('#{} {}'.format(tc, solve(new_data)))

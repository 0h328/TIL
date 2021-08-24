import sys
sys.stdin = open('input2.txt')


for tc in range(1, 11):
    N = int(input())
    stack = []
    top = -1

    arr = list(input())
    nums = []
    print(arr)
    for idx in range(N):
        if arr[idx] == '+':
            top += 1
            stack.append(arr[idx])
            while top > -1:
                nums.append(stack.pop())
                top -= 1

        elif top > -1 and arr[idx] == '*' and stack[top] == '+':
            stack.append(arr[idx])
            top += 1

        elif top > -1 and arr[idx] == '*' and stack[top] == '*':
            while stack[top] != '+' or top > -1:
                nums.append(stack.pop())
                top -= 1
        elif top == -1 and (arr[idx] == '*' or arr[idx] == '+'):
            stack.append(arr[idx])
            top += 1

        else:
            nums.append(arr[idx])

    print(stack)

import sys
sys.stdin = open('input.txt')


def Calculator(formula):
    stack = []
    nums = []

    for i in range(len(formula)):
        if formula[i] == '*':
            stack.append('*')
        elif formula[i] == '+':
            stack.append('+')
        else:
            nums.append(int(formula[i]))
            if stack and stack[-1] == '*':
                nums.append(nums.pop() * nums.pop())
                stack.pop()

    while stack:
        nums.append(nums.pop() + nums.pop())
        stack.pop()

    return nums[0]


for t in range(1, 11):
    input()
    formula = input()
    print('#{} {}'.format(t, Calculator(formula)))
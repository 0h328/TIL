new = ['9', '5', '2', '*', '+', '1', '+', '3', '3', '*', '7', '*', '6', '*', '9', '*', '1', '*', '7', '*', '+']
print(len('9+5*2+1+3*3*7*6*9*1*7'))
print(len(new))
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
        print(stack)

    return stack.pop()

print(solve(new))
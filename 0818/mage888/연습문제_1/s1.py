# https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
# https://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python
stack = []

def push(item):
    return stack.append(item)

def pop():
    if not stack:
        return

    return stack.pop()
    # 그냥 return만 쓰면 None을 반환

print(stack) # []
push(1)
push(2)
push(3)
print(stack) # [1, 2, 3]

print('---------')
# 가장 뒤(위)부터 pop
print(pop()) # 3
print(pop()) # 2
print(pop()) # 1
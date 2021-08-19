# s1.py
# 리스트 (가변크기)

stack = []

def push(item):
    stack.append(item)
    pass

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()
    pass

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
print(stack)
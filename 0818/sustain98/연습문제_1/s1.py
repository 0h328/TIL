# s1.py
# 리스트 (가변크기)

stack = []

def push(item):
    stack.append(item)

def pop():
    return stack.pop(len(stack) - 1)

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

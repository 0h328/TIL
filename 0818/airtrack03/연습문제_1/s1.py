# s1.py
# 리스트 (가변크기)

stack = []

# stack은 리스트의 주소값을 가지는 변수이므로,
# global을 쓰지 않아도 리스트 변경 가능
def push(item):
    stack.append(item)

# .pop()은 str 클래스의 메서드이므로 같은 이름으로 해도 무관
def pop():
    if len(stack) == 0:
        return None
    else:
        return stack.pop()

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

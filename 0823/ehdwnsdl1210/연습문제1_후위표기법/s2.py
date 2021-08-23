N = input()
data = input() # 중위 표기식
stack = []

# 1. 중위 표현식 -> 후위 표현식
for char in data:
    if char == '*':
        stack.append(char)
    elif char == '+':
        # stack.append(char)
        # 이 경우 고려해야 할 사항은?!
        # stack이 비어있는지?
        # stack의 가장 위(top)이 * 연산자인지 확인

    else:

# 2. 후위 표현식 -> 계산
for char in data:
    if char == '*':
    elif char == '+':
    else:

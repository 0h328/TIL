N = input()
data = input()
stack = []

#1. 중위 표현식 -> 후위 표현식

for char in data:
    if char == "*":
        stack.append(char)
    elif char == "+":

        stack.append(char)
        # 이 경우 고려해야할 사항
        # stack이 비어있는지 여부 판단 & stack의 가장 위 (top)가 * 연산자인지 확인인
    else:

#2. 후위 표현식 -> 계산

data
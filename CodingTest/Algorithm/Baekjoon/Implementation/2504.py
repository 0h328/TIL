import sys
sys.stdin = open('input.txt')

b = input()

stack = []
ans = 0
tmp = 1

for i in range(len(b)):
    if b[i] == "(":
        stack.append("(")
        tmp *= 2
    elif b[i] == "[":
        stack.append("[")
        tmp *= 3
    elif b[i] == ")":
        if not stack or stack[-1] == "[":   # [)가 되면 식이 성립되지 않음
            ans = 0
            break
        if b[i-1] == "(":   # 괄호의 쌍이 맞으면
            ans += tmp      # 누적된 합을 더해주고
        stack.pop()         # 열린 괄호 pop
        tmp //= 2           # 곱한 값만큼 나눠줌

    elif b[i] == "]":
        if not stack or stack[-1] == "(":   # (]가 되면 식이 성립되지 않음
            ans = 0
            break
        if b[i-1] == "[":
            ans += tmp
        stack.pop()
        tmp //= 3


print(0 if stack else ans)
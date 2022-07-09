import sys
sys.stdin = open('input.txt')

ans = []

while True:
    stack = []
    count = 0
    s = input()
    if '-' in s:
        break
    for i in range(len(s)):
        if not stack and s[i] == '}':
            count += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    count += len(stack)//2
    ans.append(count)

for i in range(len(ans)):
    print(i+1, '. ', ans[i], sep='')
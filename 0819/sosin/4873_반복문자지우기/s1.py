import sys
sys.stdin = open('input.txt')

# PASS
for T in range(int(input())):
    s = input()
    stack = ['']
    for w in s:
        if stack[-1] != w:
            stack.append(w)
        else:
            stack.pop()

    print('#{} {}'.format((T+1), len(stack)-1))

#1 1
#2 4
#3 11

import sys
sys.stdin = open('input.txt')

for T in range(1,11):
    N, s = input().split()
    stack = ['']
    for i in range(int(N)):
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    result = ''
    print('#{} {}'.format(T, ''.join(stack)))


#1 1234
#2 4123
#3 123123
#4 1234123123
#5 12341
#6 123535
#7 123432141
#8 231231321
#9 12312323
#10 9823
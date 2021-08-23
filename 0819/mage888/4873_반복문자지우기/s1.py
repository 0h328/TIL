import sys
sys.stdin = open('input.txt')

def cnt_stack():

    for i in range(len(word)):
        s.append(word[i])
        if len(s) >= 2 and s[-1] == s[-2]:
            s.pop()
            s.pop()

    return len(s)

T = int(input())

for tc in range(1, T+1):
    word = input()
    s = []

    print('#{} {}'.format(tc, cnt_stack()))






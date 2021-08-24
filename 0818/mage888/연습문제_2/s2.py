import sys
sys.stdin = open('input.txt')

def is_pair():

    arr = []
    for i in bracket:
        if i == '(':
            arr.append(i)
        elif i == ')':
            if arr[-1] == '(':
                arr.pop()
            # if len(arr) == 0:
            #     return False
            # pop()
            else:
                return False

    if arr:
        return False
    else:
        return True

T = 2

for tc in range(1, T+1):
    bracket = input()

    print('#{} {}'.format(tc, is_pair()))

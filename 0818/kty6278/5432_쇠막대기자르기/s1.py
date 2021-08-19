import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    iron = input()
    cnt = 0
    my_list = []

    for i in range(len(iron)):
        if iron[i] == '(':
            my_list.append(iron[i])
        elif iron[i] == ')':
            my_list.pop()
            if iron[i - 1] == '(':   # ()인 경우 레이저
                cnt += len(my_list)
            else:
                cnt += 1             # ))인 경우 끝점
    print(cnt)
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_str = input()
    i = 0
    while True:
        if i == len(my_str) - 1:
            break
        if my_str[i] == my_str[i+1]:
            str1 = my_str[0:i]
            str2 = my_str[i+2:]
            my_str = str1 + str2
            i = 0
        else:
            i += 1


    print('#{} {}'.format(tc, len(my_str)))


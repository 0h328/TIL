import sys
sys.stdin = open('input.txt')

T = int(input())

for z in range(T):
    N,M = map(int,input().split())

    input_list = [input() for _ in range(N)]
    find_list = []

    for k in input_list:
        for i in range(len(k)):
            if k[i] == str(1):
                end = i
                find_list = k
    password_list = find_list[end-55:end+1]

    find_password_list = [['0001101'],['0011001'],['0010011'],['0111101'],['0100011'],['0110001'],['0101111'],['0111011'],['0110111'],['0001011']]

    check = 0
    ans = 0
    for b in range(1,9):
        temp_list = password_list[b*7-7:b*7]
        for c in range(len(find_password_list)):
            if find_password_list[c] == [temp_list]:
                if b % 2 == 1:
                    check += c*3
                    ans += c
                else:
                    check += c
                    ans += c
    if check % 10 == 0:
        print('#{} {}'.format(z+1,ans))
    else:
        print('#{} {}'.format(z+1,0))
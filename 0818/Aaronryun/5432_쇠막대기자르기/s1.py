import sys

sys.stdin = open('input.txt')

for test in range(int(input())):
    data = input()

    cnt = 0
    answer = 0

    for i in range(len(data)):
        if data[i] == '(':
            cnt+=1
        else:
            if data[i-1] == '(':
                cnt-=1
                answer+=cnt
            else:
                cnt-=1
                answer+=1

    print('#{} {}'.format(test+1,answer))
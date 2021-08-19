import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(num):
    res_list = [1] * num
    if num == 1:
        return res_list
    else:
        for i in range(1, num-1):
            res_list[i] = pascal(num-1)[i-1] + pascal(num-1)[i]
    return res_list

for case in range(T):
    N = int(input())

    print('#{}'.format(N))
    start = 1
    while start <= N:
        for i in pascal(start):
            print(i, end=' ')
        print()
        start += 1

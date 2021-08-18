import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(num):
    res = []
    res_list = [1] * num
    if num == 1:
        res.append(res_list)
        return res
    else:
        for i in range(1,num-1):
            res_list[i] = pascal(num-1)[-1][i-1] + pascal(num-1)[-1][i]
        res.append(res_list)
    return pascal(num-1) + res


for case in range(T):
    N = int(input())
    res = []
    print('#{}'.format(case + 1))
    for i in pascal(N):
        for j in i:
            print(j, end=' ')
        print()



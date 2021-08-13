import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())

    num_list = [2, 3, 5, 7, 11]
    count_list = []
    for i in num_list:
        cnt = 0
        while not(N%i):
            if N%i ==0:
                cnt += 1
                N = N//i
        count_list.append(cnt)
    res = ' '.join(map(str,count_list))

    print('#{} {}'.format(case+1,res))


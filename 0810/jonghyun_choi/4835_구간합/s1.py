import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    ind = 0
    max_part = sum([a[i] for i in range(ind,ind+M)])
    min_part = sum([a[i] for i in range(ind,ind+M)])
    while ind < N-M+1:
        cal_list = [a[i] for i in range(ind,ind+M)]
        if sum(cal_list) > max_part:
            max_part = sum(cal_list)
        if sum(cal_list) < min_part:
            min_part = sum(cal_list)
        ind += 1
    gap = (max_part - min_part)

    print('#{} {}'.format(case+1,gap))



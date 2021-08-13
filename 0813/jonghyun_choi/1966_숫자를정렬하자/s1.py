import sys
sys.stdin = open('input.txt')

T = int(input())

for Case in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))

    for i in range(len(num_list)-1):
        min_num = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min_num]:
                min_num = j
        num_list[i], num_list[min_num] = num_list[min_num], num_list[i]
    res = ' '.join(map(str,num_list))
    print('#{} {}'.format(Case+1,res))
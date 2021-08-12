import sys
sys.stdin = open('input.txt')

T = int(input())

for Case in range(T):
    N = int(input())
    data_list = list(map(int,input().split()))

    for i in range(len(data_list)-1):
        min_num = max_num = i
        if i%2:
            for j in range(i+1,len(data_list)):
                if data_list[j] < data_list[min_num]:
                    min_num = j
            data_list[i], data_list[min_num] = data_list[min_num], data_list[i]
        else:
            for j in range(i+1,len(data_list)):
                if data_list[j] > data_list[max_num]:
                    max_num = j
            data_list[i], data_list[max_num] = data_list[max_num], data_list[i]
    res = ' '.join(map(str,data_list[:10]))
    print('#{} {}'.format(Case+1, res))







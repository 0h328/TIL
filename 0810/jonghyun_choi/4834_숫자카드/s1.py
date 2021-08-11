import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())
    number_list = list(map(int,''.join(input())))
    # print(number_list)
    dic_cnt = {}
    for i in number_list:
        if i not in dic_cnt:
            dic_cnt[i] = 1
        else:
            dic_cnt[i] += 1
    # print(dic_cnt)
    dic_to_list = [(key,value) for key,value in dic_cnt.items()]
    # print(dic_to_list)
    sort_list = sorted(dic_to_list, key=lambda x:(x[1],x[0]),reverse=True)[0]
    # print(sort_list)

    print('#{} {} {}'.format(case+1,sort_list[0],sort_list[1]))

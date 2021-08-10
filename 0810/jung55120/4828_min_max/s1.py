import sys
sys.stdin = open('input.txt')

num = int(input())
for tc in range(num):
    cnt = int(input())
    new_list = list(map(int, input().split()))
    max_num = new_list[0]
    min_num = new_list[0]
    for i in range(1, len(new_list)):
        if new_list[i] > max_num :
            max_num = new_list[i]
    for j in range(1, len(new_list)):
        if new_list[j] < min_num :
            min_num = new_list[j]

    print('#{0} {1}'.format(tc+1, max_num-min_num))
import sys
sys.stdin = open('input.txt')


test_case = int(input())

cnt = 0

for tc in range(1, test_case+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(10):
        idx = i
        for j in range(i, n):
            if not i%2 and num_list[idx] < num_list[j]:
                idx = j
            elif i%2 and num_list[idx] > num_list[j]:
                idx = j
        num_list[i], num_list[idx] = num_list[idx], num_list[i]

    print('#{} {} {} {} {} {} {} {} {} {} {}'.format(tc, *num_list[:10]))
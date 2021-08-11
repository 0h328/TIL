import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    minus_list = [my_list[0]]
    for i in range(M-1):
        minus_list.append(my_list[i+1] - my_list[i])
    minus_list.append(N-my_list[M-1])

    for i in range(len(minus_list)):
        if minus_list[i] > K:
            ans = 0
            break
    else:
        minus_sum_list = []
        for k in range(2, len(minus_list) + 1):
            for j in range(0, len(minus_list) - (k - 1)):
                minus_sum_list.append([k, sum(minus_list[j:j+k])])

        cnt = 0
        for i in range(K, 1, -1):
            for num in minus_sum_list:
                if num[1] == i:
                    cnt += num[0]-1

    ans = (len(minus_list) - 1) - cnt

    print('#{} {}'.format(test_case, ans))


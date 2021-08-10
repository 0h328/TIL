import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    my_total = 0
    my_sum_list = []
    for i in range(N-M+1):
         my_total = sum(L[i : i+M])
         my_sum_list.append(my_total)

    cal = max(my_sum_list) - min(my_sum_list)

    print('#{} {}'.format(t+1, cal))
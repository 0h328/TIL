import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    N_list = list(map(int,input().split()))
    M_list = list(map(int,input().split()))
    ans = 0
    for i in range(M):
        M_max = max(M_list)
        M_list.remove(M_max)
        temp_k = 0
        for k in N_list:
            if k <= M_max and temp_k < k:
                temp_k = k
        if temp_k in N_list:
            N_list.remove(temp_k)
        ans += temp_k

    print('#{} {}'.format(tc,ans))
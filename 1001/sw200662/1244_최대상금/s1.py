import sys

sys.stdin = open('input.txt')

T = int(input())

def sum_list(num):
    global ans
    M = len(num)
    temp_num = 0
    for i in range(M):
        temp_num += int(num[i]) * 10 ** (M-i-1)
    if temp_num > ans:
        ans = temp_num
    return

def dfs(a,k):
    if k == M:
        sum_list(num_list)
        return

    else:
        for i in range(length):
            for j in range(i+1, length):
                a[i], a[j] = a[j], a[i]
                num = int(''.join(map(str, a)))
                if (num, k) not in visited:
                    visited.add((num,k))
                    dfs(a,k+1)
                a[i], a[j] = a[j], a[i]



for tc in range(1, T + 1):
    ans = 0
    N, M = map(int, input().split())
    num_list = []
    num_list.extend(str(N))
    length = len(num_list)
    cnt = 0
    visited = set()
    dfs(num_list,0)
    print('#{} {}'.format(tc,ans))






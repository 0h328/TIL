import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

def counting_sort(num):
    cnt = [0] * max(num)

    for i in range(len(num)):
        cnt[num[i]-1] += 1

    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]

    tmp = [0] * len(num)
    for k in range(len(num)-1, -1, -1):
        cnt[num[k]-1] -= 1
        tmp[cnt[num[k]-1]] = num[k]
    return tmp



print(counting_sort(num))

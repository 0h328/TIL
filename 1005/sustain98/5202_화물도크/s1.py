import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    reserv = []
    for _ in range(n):
        s, e = map(int, input().split())
        reserv.append((s, e))
    reserv.sort(key=lambda x: x[0])
    len_list = [0]*n

    for i in range(n-1, -1, -1):
        len_list[i] += 1
        for j in range(i-1, -1, -1):
            if reserv[j][1] <= reserv[i][0] and len_list[j] < len_list[i]:
                len_list[j] = len_list[i]

    print('#{} {}'.format(idx, max(len_list)))



import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    alpha_list = [list(input()) for _ in range(N)]
    zip_list = list(zip(*alpha_list))
    i = 0
    while i < N - M + 1:
        for j in alpha_list:
            if j[i:i+M] != j[i:i+M][::-1]:
                continue
            else:
                print('#{} {}'.format(case + 1, ''.join(j[i:i+M])))
                break
        i += 1

    k = 0
    while k < N - M + 1:
        for j in zip_list:
            if j[k:k+M] != j[k:k+M][::-1]:
                continue
            else:
                print('#{} {}'.format(case + 1, ''.join(j[k:k+M])))
                break
        k += 1


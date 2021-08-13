import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    M = len(L)
    half = int(M / 2) # float다...

    for i in range(M - 1): # sorted(), .sort() 다 안됨 / 선택정렬
        min_idx = i
        for j in range(i + 1, M):
            if L[min_idx] > L[j]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]

        my_list = []
        for k in range(half):
            my_list.append(L[-k-1]) # 큰거 추가가 먼저
            my_list.append(L[k])

    # print('#{} {}'.format(tc + 1, my_list[0:10])) 안됩니더
    print('#{}'.format(tc + 1), end= ' ')
    for l in my_list[0:10]:
        print(l, end=' ')
    print()
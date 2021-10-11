import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    temp = 1

    for i in H:
        temp |= temp << i

    bi = bin(temp)
    for j in range(len(bi)-B):
        if bi[j] == '1':
            ans = len(bi) - (j+1) - B

    # bi = bin(temp)[::-1]
    # for j in range(B, len(bi)):
    #     if bi[j] == '1':
    #         ans = j
    #         break

    print('#{} {}'.format(t, ans))
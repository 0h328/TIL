import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    ans = -1

    i = 0
    while i < N-1:
        j = i + 1
        while j < N:
            new_num = str(num[i] * num[j])
            for k in range(1, len(new_num)+1):
                if k == len(new_num):
                    temp = int(new_num)
                    if temp > ans:
                        ans = temp
                        break
                elif int(new_num[k]) < int(new_num[k-1]):
                    break
            j += 1
        i += 1

    print('#{} {}'.format(t, ans))
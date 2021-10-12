import sys
sys.stdin = open('input.txt')

def checking(M, k):
    for idx in range(len(M)-1):
        if M[idx] == M[idx+1]:
            M.pop(idx)
            M.pop(idx)
            k = len(M)
            return checking(M, k)
    if len(M) == k:
        return M


for tc in range(10):
    N, M = input().split()
    N = int(N)
    M = list(M)

    ans = checking(M, N)
    print('#{} '.format(tc+1), end='')
    for n in ans:
        print(n, end='')
    print()




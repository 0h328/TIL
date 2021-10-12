import sys
sys.stdin = open('input.txt')

def checking(chrs, N):
    for idx in range(N-1):
        if chrs[idx] == chrs[idx + 1]:
            chrs.pop(idx)
            chrs.pop(idx)
            N = len(chrs)
            return checking(chrs, N)
    if len(chrs) == N:
        return chrs

T = int(input())
for tc in range(1, T+1):
    chrs = list(input())
    N = len(chrs)
    ans = len(checking(chrs, N))

    print('#{} {}'.format(tc, ans))


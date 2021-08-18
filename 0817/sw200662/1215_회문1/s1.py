import sys
sys.stdin = open('input.txt')

for c in range(10):
    m = int(input())
    list_word = [input() for _ in range(8)]
    col_list_word = list(zip(*list_word))
    ans = 0
    for k in range(8):
        for i in range(8-m+1):
            A = list_word[k][i:i+m]
            B = A[::-1]
            if A == B:
                ans += 1
            C = col_list_word[k][i:i+m]
            D = C[::-1]
            if C == D:
                ans += 1
    print('#{} {}'.format(c+1,ans))
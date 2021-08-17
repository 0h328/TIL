import sys
sys.stdin = open('input.txt')

for c in range(1,11):
    T = int(input())
    list_word = [input() for _ in range(100)]
    col_list_word = list(zip(*list_word))
    ans = 0
    for m in range(1,100):
        for k in range(100):
            for i in range(100-m+1):
                test_word = ''
                A = list_word[k][i:i+m]
                B = A[::-1]
                if A == B and ans < len(A):
                    ans = len(A)
                C = col_list_word[k][i:i+m]
                D = C[::-1]
                if C == D and ans < len(C):
                    ans = len(C)
    print('#{} {}'.format(c,ans))









import sys

sys.stdin = open('input.txt')

for c in range(1, 11):
    T = int(input())
    list_word = [input() for _ in range(100)]
    col_list_word = list(zip(*list_word))
    ans = 0
    check = 0
    for m in range(100, 1, -1): # for m in range(2,101)
        if check == 1: # 높은곳부터 나오기
            break
        for k in range(100):
            for i in range(100 - m + 1):
                A = list_word[k][i:i + m]
                B = A[::-1]
                if A == B: #if A == B and ans < len(A):
                    ans = m
                    check = 1
                C = col_list_word[k][i:i + m]
                D = C[::-1]
                if C == D and ans < len(C): # if C == D and ans < len(C):
                    ans = m
                    check = 1
    print('#{} {}'.format(c, ans))

# https://en.wikipedia.org/wiki/Longest_palindromic_substring

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    p = [input() for _ in range(100)]
    pal_len = 1

    for i in range(100):
        for j in range(100):
            for k in range(100-j+1):
                for l in range(j//2):
                    if p[i][k+l] != p[i][k+j-1-l]:
                        break
                else:
                    if pal_len < j:
                        pal_len = j

                for l in range(j//2):
                    if p[k+l][i] != p[k+j-1-l][i]:
                        break
                else:
                    if pal_len < j:
                        pal_len = j

    print('#{} {}'.format(tc, pal_len))


    # c_a = []
    # for i in range(len(r_a)):
    #     c_a_word = ''
    #     for j in range(len(r_a[i])):
    #         c_a_word += r_a[j][i]
    #     c_a.append(c_a_word)


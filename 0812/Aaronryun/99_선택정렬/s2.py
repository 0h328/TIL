import sys

sys.stdin = open('input2.txt')

T = int(input())

for test in range(T):
    p = input()
    t = input()
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        print('#{} {}'.format(test + 1, 1))
    else:
        print('#{} {}'.format(test + 1, 0))

        # p = 'is'
        # t = 'This is a book~!'
        # M = len(p)
        # N = len(t)
        #
        # def BruteForce(p,t):
        #     i=0
        #     j=0
        #     while j<M and i<N:
        #         if t[i]!=p[j]:
        #             i=i-j
        #             j=-1
        #         i+=1
        #         j+=1
        #     if j ==M:return i-M
        #     else:return -1
        #
        # print(BruteForce(p,t))

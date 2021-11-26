import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    Pattern = input()
    Target = input()
    M = len(Pattern)
    N = len(Target)

    ans = 0
    for i in range(0, N-M+1):
        my_str = ''
        for j in range(i, i+M):
            my_str += Target[j]
        if my_str == Pattern:
            ans = 1
            break


    print('#{} {}'.format(test_case, ans))



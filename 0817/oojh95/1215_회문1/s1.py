import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    M = int(input())
    words = [list(input()) for _ in range (8)]

    result = 0
    if M == 1:
        result = 128
    else:
        for i in range(8):
            for j in range(8 - M + 1):
                for k in range (M // 2):
                    if words[i][j + k] != words[i][j + M - 1 - k]:
                        break
                else:
                    result += 1
                for k in range(M // 2):
                    if words[j + k][i] != words[j + M - 1 - k][i]:
                        break
                else:
                    result +=1
    print('#{} {}'.format(test_case, result))

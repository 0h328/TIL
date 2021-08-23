import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    result =[]
    for i in range(15):
        for j in range(5):
            try:
                result.append(words[j][i])
            except:
                continue
    print('#{}'.format(test_case),end=' ')
    print(*result, sep='')
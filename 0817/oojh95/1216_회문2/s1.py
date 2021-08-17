import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = input()
    words = [list(input()) for _ in range(100)]

    result = 1
    for l in range(2, 100):
        for i in range(100):
            for j in range(100 - l + 1):
                for k in range(l // 2):
                    if words[i][j + k] != words[i][j + l - 1 - k]:
                        break
                else:
                    result = l
                for k in range(l // 2):
                    if words[j + k][i] != words[j + l - 1 -k][i]:
                        break
                else:
                    result = l
                    break
    print('#{} {}'.format(T, result))




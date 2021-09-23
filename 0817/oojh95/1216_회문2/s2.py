import sys
sys.stdin = open('input.txt')

def palindrome(words):
    for l in range(100, 1, -1):
        for i in range(100):
            for j in range(100 - l + 1):
                for k in range(l // 2):
                    if words[i][j + k] != words[i][j + l - 1 - k]:
                        break
                else:
                    return l
                for k in range(l // 2):
                    if words[j + k][i] != words[j + l - 1 -k][i]:
                        break
                else:
                    return l
    else:
        return 1



for _ in range(10):
    T = input()
    words = [list(input()) for i in range(100)]
    result = palindrome(words)
    print('#{} {}'.format(T, result))




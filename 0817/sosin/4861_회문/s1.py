import sys
sys.stdin = open('input.txt')

def find_palindrome(arr, N, M):
    arr_T = list(zip(*arr))
    for i in range(N):
        for j in range(N-M+1):
            words = arr[i][j:j+M]
            words_T = arr_T[i][j:j+M]
            if words == words[::-1]:
                return ''.join(words)
            if words_T == words_T[::-1]:
                return ''.join(words_T)

for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = find_palindrome(arr, N, M)
    print('#{} {}'.format((t+1), result))

#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT

# print('aba' == 'aba'[::-1])
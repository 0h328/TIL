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
    return ''

for _ in range(10):
    T = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    max_length = 1
    for i in range(2, 100):
        if i > max_length + 2:
            break
        if find_palindrome(arr, N, i):
            max_length = i
    print('#{} {}'.format((T), max_length))

#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18
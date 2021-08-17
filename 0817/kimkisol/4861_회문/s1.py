import sys
sys.stdin = open('input.txt')

def is_palindrome(list_a, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            # 행 별로 확인
            for m in range(M // 2):  # 앞뒤로 하나씩 일치여부 확인
                if list_a[i][j + m] != list_a[i][j + M - 1 - m]:
                    break
            else:
                return ''.join(list_a[i][j:j + M])
            # 열 별로 확인
            for m in range(M // 2):  # 앞뒤로 하나씩 일치여부 확인
                if list_a[j + m][i] != list_a[j + M - 1 - m][i]:
                    break
            else:
                result_col = ''
                for m in range(M):
                    result_col += list_a[j + m][i]
                return result_col
    return False

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    list_a = [list(input()) for _ in range(N)]
    print('#{} {}'.format(t, is_palindrome(list_a, N, M)))
import sys
sys.stdin = open('input.txt', encoding='UTF8')

def longest_palindrome(list_a):
    longest = 1
    for i in range(100): #행
        for k in range(longest + 1, 101): #제일 긴 문자열
            for j in range(100 - k + 1): #열
                #행 별로 확인
                for m in range(k // 2): #앞뒤로 하나씩 일치여부 확인
                    if list_a[i][j + m] != list_a[i][j + k - 1 - m]:
                        break
                else:
                    longest = k
                    break
                #열 별로 확인(i가 열로, j가 행으로 바뀜)
                for m in range(k // 2): #앞뒤로 하나씩 일치여부 확인
                    if list_a[j + m][i] != list_a[j + k - 1 - m][i]:
                        break
                else:
                    longest = k
                    break
    return longest

for t in range(1, 11):
    input()
    list_a = [list(input()) for _ in range(100)]
    print('#{} {}'.format(t, longest_palindrome(list_a)))
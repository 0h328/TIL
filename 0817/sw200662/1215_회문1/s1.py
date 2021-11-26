import sys
sys.stdin = open('input.txt')

for c in range(10):
    m = int(input())
    list_word = [input() for _ in range(8)]  #가로
    col_list_word = list(zip(*list_word)) # 세로
    ans = 0
    for k in range(8):
        for i in range(8-m+1):
            A = list_word[k][i:i+m] # slicing을 통해 원하는만큼 잘라내고
            B = A[::-1] # 회문인지 판별하기 위하여 reverse
            if A == B: # 만약 같다면, ans + 1
                ans += 1
            C = col_list_word[k][i:i+m]
            D = C[::-1]
            if C == D:
                ans += 1
    print('#{} {}'.format(c+1,ans))
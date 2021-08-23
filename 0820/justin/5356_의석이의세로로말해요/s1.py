import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    word = [0] * 5
    max_len = 0
    for i in range(5):                
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])    # 최대 길이 찾기

    print('#{}'.format(tc), end=' ')
    for i in range(max_len):          # 최대 길이만큼 반복을 돌며 세로로 글자 읽기
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end='')
    print()
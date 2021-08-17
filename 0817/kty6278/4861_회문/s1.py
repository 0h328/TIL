import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):                                                     # 테스트 케이스를 불러온다
    row, length = map(int, input().split())                             # row는 행과 열, length는 찾아야 하는 단어의 길이

    word = []
    for _ in range(row):                                                # word 리스트에 row*row개의 글자를 받아들인다.
        word.append(input())
    # print(word)
    result = []                                                         # 가로에 회문이 존재하는가?
    for i in range(row):                                                # row(행) 만큼 반복
        for j in range(row - length + 1):                               # row가 '20'이고 찾는 단어의 길이가 '13'인 경우 '8'번 반복 (마지막 필요없는 부분 제외)
            if word[i][j:j+length] == word[i][j:j+length][::-1]:        # word의 첫 행에서 원하는 글자 길이만큼과 역순이 같은지 판단
                result.append(word[i][j:j + length])                    # 같은 경우 문자열 추가
    # print(result)

    for i in range(row):                                                # row(행) 만큼 다시 반복 열에 맞게 부를 예정
        for j in range(row - length + 1):
            new_word = []                                               # 세로에 회문이 존재하는가?
            for k in range(length):
                new_word.append(word[k+j][i])                           # 1,0/ 2,0 ..../ 2,0 3,0..... row-length-1만큼 반복하면서 열에 맞게 word불러옴
            # zip 함수 사용해보기
            # print(new_word)
            if new_word == new_word[::-1]:                              # 불러온 word가 역순이랑 같은지 비교
                final = ''.join(new_word)
                result.append(final)                                    # 같은 경우 추가
    # print(result)
    print('#{}'.format(tc + 1), end = ' ')
    print(*result)




import sys
sys.stdin = open('input.txt')


T = int(input())                                 # 테스트 케이스 받아오기
for tc in range(T):                              # 테스트 케이스 만큼 반복 진행
    find_word = list(set(input()))               # 반복되는 문자가 존재하는 문자열
    word = input()                               # 반복되는 전체 문자열


    cnt_list = []                                # 개수를 센 후 저장하는 리스트
    for j in range(len(find_word)):                # 중복 없는 단어별로 반복
        cnt = 0                                  # 단어의 종류별로 초기화
        for k in range(len(word)):               # 전체 문자열의 길이 만큼 반복
            if find_word[j] in word[k]:            # 문자가 문자열에 존재하는지 파악
                cnt += 1                         # 존재하는 경우 +1
                # print(cnt)
        cnt_list.append(cnt)             # 문자별로 cnt 한 것들 리스트에 저장
    # print(cnt_list)
    print('#{} {}'.format(tc + 1, max(cnt_list)))
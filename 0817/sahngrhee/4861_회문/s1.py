def Palindrome(word): #Palindrome 확인하는 함수 생성
    for i in range(len(word)//2): # word 길이의 절반만 확인
        if word[i] != word[len(word)-1-i]: # 처음과 마지막 값 비교 -> 양 쪽 끝에서 안으로 하나씩 줄여가면서 비교
            return False # 하나라도 다른게 있으면 False
    else:
        return True # 비교가 전부 다 만족하면 True

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    chars_list = [list(input()) for _ in range(N)] # 2차원 행렬으로 받음
    chars_list_vertical = [] # zip 써서 행과 열을 서로 교환
    for ele in zip(*chars_list):
        chars_list_vertical.append(list(ele))
    #chars_list_vertical = list(zip(*chars_list))

    ans = 0 # 답 0으로 초기화
    for chars in chars_list: # 수평 리스트에서
        for i in range(N-M+1): # M 크기로 한칸씩 이동하면서 확인할때 인덱스 크기
            word = '' # 빈 str 초기화
            for j in range(i, i+M): # M 크기로 한칸씩 이동하면서
                word += chars[j] # 글자 생성
        if Palindrome(word): # 해당 글자가 회문이면
            ans = word # 답은 해당 글자

    for chars in chars_list_vertical: # 수직 리스트에서
        for i in range(N-M+1): # M 크기로 한칸씩 이동하면서 확인할때 인덱스 크기
            word = '' # 빈 str 초기화
            for j in range(i, i+M): # M 크기로 한칸씩 이동하면서
                word += chars[j] # 글자 생성
        if Palindrome(word): # 해당 글자가 회문이면
            ans = word # 답은 해당 글자

    print('#{} {}'.format(test_case, ans)) # 답안 출력


def Palindrome(word): #Palindrome 확인하는 함수 생성
    for i in range(len(word)//2): # word 길이의 절반만 확인
        if word[i] != word[len(word)-1-i]: # 처음과 마지막 값 비교 -> 양 쪽 끝에서 안으로 하나씩 줄여가면서 비교
            return False # 하나라도 다른게 있으면 False
    else:
        return True # 비교가 전부 다 만족하면 True

import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    T = int(input())
    char_list = [list(input()) for _ in range(100)]
    char_list_vertical = []
    for ele in zip(*char_list):
        char_list_vertical.append(list(ele))

    row_max = 0
    column_max = 0
    for M in range(1, 101):
        for i in range(100):
            for j in range(100-M+1):
                my_str = ''
                for k in range(j, j+M):
                    my_str += char_list[i][k]
                if Palindrome(my_str):
                    row_max = M
                    break

    for M in range(1, 101):
        for i in range(100):
            for j in range(100-M+1):
                my_str = ''
                for k in range(j, j+M):
                    my_str += char_list_vertical[i][k]
                if Palindrome(my_str):
                    column_max = M
                    break

    if row_max > column_max:
        ans = row_max
        print('#{} {}'.format(test_case, ans))
    else:
        ans = column_max
        print('#{} {}'.format(test_case, ans))

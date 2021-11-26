import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    test, length = map(str, input().split())
    number = list(map(str, input().split()))  # 리스트로 받아오기!!!!
    # print(number)
    number_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    int_length = int(length)
    new_list = []
    final_list = []

    for i in range(int_length):  # 문자를 숫자로, 숫자를 정렬
        for j in range(10):
            if number[i] == number_list[j]:
                new_list.append(num_list[j])
                new_list.sort()

    for k in range(int_length):  # 정렬된 숫자를 문자로 변형
        for l in range(10):
            if new_list[k] == num_list[l]:
                final_list.append(number_list[l])
    print('#{}'.format(tc + 1))
    print(' '.join(final_list))






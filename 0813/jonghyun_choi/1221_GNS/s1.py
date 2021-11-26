import sys
sys.stdin = open('input.txt')

T = int(input())
str_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(T):
    case_number, len_number = input().split()
    number_list = list(input().split())
    i = 0
    j = 0
    move_index = 0
    while i < len(str_number)-1:                    # EGT까지만 정렬해주면 자동으로 NIN은 정렬된다.
        while j < int(len_number):                  # 전체 len_number 까지 도달하면 비교가 완료
            if number_list[j] == str_number[i]:     # 만약 해당 str 와 number_list의 값이 같으면 swap
                number_list[move_index] , number_list[j] = number_list[j], number_list[move_index]
                move_index += 1                     # swap할 인덱스는 + 1 (이미 앞 index는 swap으로 인해 정렬 완료되었으므로)
            j += 1
        j = move_index                              # zero를 다 찾았으므로 one을 찾기 시작하면 되는데 one은 zero가 있는 인덱스부터 찾을 필요가 없으므로 j를 move_index로 업데이트
        i += 1
    print(case_number)
    print(' '.join(number_list))
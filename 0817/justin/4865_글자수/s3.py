import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    check_arr = [0] * 26 # str1 해당 글자가 있는지 체크
    count_arr = [0] * 26 # 해당 글자 카운트
    for chr in str1:                      # str1을 순회하면서 알파벳 체크
        check_arr[ord(chr)-ord('A')] = 1

    # print(check_arr)
    for chr in str2:
        if check_arr[ord(chr)-ord('A')]:  # 있는 경우
            count_arr[ord(chr)-65] += 1   # ord('A') -> 65
    # print(count_arr)

    ans = max(count_arr)
    print('#{} {}'.format(tc, ans))
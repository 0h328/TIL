import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    my_dict = {}                        # 키 -> 문자, value -> 카운트한 수
    for key in set(str1):               # str1의 문자를 가진 딕셔너리 0으로 초기화
        my_dict[key] = 0

    for key in str2:
        if key in my_dict:              # 반복을 돌며 딕셔너리에 cnt 누적
            my_dict[key] += 1

    ans = 0
    for my_count in my_dict.values():   # 최댓값
        if ans < my_count:
            ans = my_count

    print('#{} {}'.format(tc, ans))
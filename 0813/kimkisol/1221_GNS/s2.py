import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#각 숫자형 문자(key) : 숫자값(value)으로 딕셔너리 생성
nums_match = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())

for _ in range(T):
    test_case, N = input().split()
    str_nums = input().split()
    print(str_nums)

    #nums_match 딕셔너리의 value값을 기준으로 오름차순 정렬
    new_str_nums = sorted(str_nums, key=lambda x: nums_match[x])

    print(test_case)
    #언패킹하여 숫자 하나씩 꺼내서 출력
    print(*new_str_nums)
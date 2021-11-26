import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

nums_match = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for t in range(1, T+1):
    input()
    str_nums = list(input().split())
    cnt_nums = [0] * 10 #str_nums가 각각 몇개씩 있는지 카운트하는 리스트

    # str_num의 idx값을 가져와 cnt_nums의 해당하는 카운트 값 +1
    for str_num in str_nums:
        cnt_nums[nums_match.index(str_num)] += 1

    print('#{}'.format(t))
    for idx, str_num in enumerate(nums_match): #0, 'ZRO' / 1 'ONE' ...
        for _ in range(cnt_nums[idx]): #해당값을 카운트해준 만큼 print 반복
            print(str_num, end=' ')
    print()

import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    tc, length = list(input().split())
    str_list = input().split()
    new_list = []

    # 어떻게 해야 문자를 숫자와 대응시킬 수 있을까?
    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(10):                 # ZRO 와 비교, ONE 과 비교, ...
        for strs in str_list:
            if strs == order[i]:        # 문자열에 ZRO 가 있나? ONE 이 있나? ...
                new_list.append(strs)   # 새로운 리스트 오른쪽에 추가
    print(tc)
    print(*new_list)                    # 리스트의 요소 언패킹해서 출력

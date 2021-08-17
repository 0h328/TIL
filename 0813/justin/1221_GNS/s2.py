import sys
sys.stdin =open('input.txt')
T = int(input())
digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T+1):
    temp = input()
    data = list(map(str, input().split()))
    count = [0 for _ in range(10)]
    for i in range(len(data)):                     # count 값 생성 & 값 채워넣기
        if data[i] == digit[0]: count[0] += 1
        elif data[i] == digit[1]: count[1] += 1
        elif data[i] == digit[2]: count[2] += 1
        elif data[i] == digit[3]: count[3] += 1
        elif data[i] == digit[4]: count[4] += 1
        elif data[i] == digit[5]: count[5] += 1
        elif data[i] == digit[6]: count[6] += 1
        elif data[i] == digit[7]: count[7] += 1
        elif data[i] == digit[8]: count[8] += 1
        elif data[i] == digit[9]: count[9] += 1

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        for _ in range(count[i]):       # 카운트 되어있는 횟수만큼 반복
            print(digit[i], end=' ')
    print()
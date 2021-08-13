import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    case, num = map(str, input().split()) # 이 부분 안 쓸 거임
    num_list = list(map(str, input().split()))
    alphabet = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = [0] * 10

    for char in num_list:
        cnt[alphabet.index(char)] += 1

    print('#{}'.format(t))

    for i in range(10):
        print('{} '.format(alphabet[i]) * cnt[i])
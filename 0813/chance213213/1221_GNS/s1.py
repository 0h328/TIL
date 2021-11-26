import sys
sys.stdin = open('input.txt')

N = int(input())
basic_arr = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(N):
    a, b = input().split()
    arr = list(map(str, input().split()))

    cnt_arr = [0] * 10                          #각 각 카운트
    for i in range(10):
        cnt_arr[i] += arr.count(basic_arr[i])   #arr에 들어있는 문자 횟수 각각 더하기

    ans = ''
    for i in range(10):
        ans += (basic_arr[i] + ' ') * cnt_arr[i] #'ZRO'횟수 만큼 더하기 쭈욱 반복

    print('{}'.format(a))           #이 부분은 줄바꿈 다른 방법 없나?
    print('{}'.format(ans))





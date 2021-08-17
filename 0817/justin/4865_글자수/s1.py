import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = [0] * len(str1)           # str1 각 문자에 카운트하는 배열
    for i in range(len(str1)):      # str1의 길이만큼 순회
        for j in range(len(str2)):  # str2에 들어있는 str1[i]의 문자 개수 확인
            if str1[i] == str2[j]:
                cnt[i] += 1

    ans = 0
    for i in range(len(cnt)):       # 가장 큰 값 찾기
        if ans < cnt[i]:
            ans = cnt[i]

    print('#{} {}'.format(tc, ans))
import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    num, cnt = input().split() # 숫자판의 정보, 교환횟수
    cnt = int(cnt)
    now = set([num])  # 중복없이 뽑아낸다 {'123'}
    result = set() # 중복없이 결과물 담으려고
    for _ in range(cnt):
        while now:
            s = list(now.pop())  # 리스트 형식으로 존재하는 값 뽑아낸다 123 // ['1', '2', '3']
            #print(s)
            for i in range(len(num)-1):
                for j in range(i + 1, len(num)):
                    s[i], s[j] = s[j], s[i] # 값 변경
                    result.add(''.join(s)) # 변경한 값 result에 저장
                    s[i], s[j] = s[j], s[i] # 변경한거 되돌리기
        now, result = result, now

    print('#{} {}'.format(tc+1, max(now)))
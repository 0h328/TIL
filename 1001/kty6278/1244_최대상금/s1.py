import sys
sys.stdin = open('input.txt')

# 모르겠어서 찾아본 코드 ㅠ

for tc in range(int(input())):
    num, cnt = input().split() # 숫자판의 정보, 교환횟수
    cnt = int(cnt)

    now = set([num])  # 중복없이 딕셔너리 형태로 뽑아낸다 {'123'}
    result = set() # 중복없이 결과물 담으려고
    for i in range(cnt):
        while now:
            s = now.pop()  # 리스트에 존재하는 값 뽑아낸다 123
            s = list(s) # 리스트 형식으로 담는다 ['1', '2', '3']

            for i in range(len(num)):
                for j in range(i + 1, len(num)):
                    s[i], s[j] = s[j], s[i] # 값 변경
                    result.add(''.join(s)) # 변경한 값 nxt에 저장
                    s[i], s[j] = s[j], s[i]
        now, result = result, now

    print('#{} {}'.format(tc+1, max(now)))
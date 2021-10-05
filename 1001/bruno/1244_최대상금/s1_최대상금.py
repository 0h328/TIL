import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    num, cnt = input().split()  # num : 78466, cnt : 2
    ready = set([num])      # 다음 교환을 기다리는 장소  /  {'78466'}
    change = set()          # 이번 교환이 완료되면 저장되는 장소  /  {'87466', '48766', '68476', ...}
    for _ in range(int(cnt)):    # 교환횟수만큼 반복
        while ready:        # ready에서 하나씩 뽑아서 자리교환
            s = ready.pop()             # '78466'
            s = list(s)                 # ['7', '8', '4', '6', '6']

            for i in range(len(num)-1):   # 두 개씩 계속 바꿔보자
                for j in range(i+1, len(num)):
                    s[i], s[j] = s[j], s[i]
                    change.add(''.join(s))      # 바꾼 결과가 새로운 값일 때만 change에 추가
                    s[i], s[j] = s[j], s[i]     # 원상복구 시키고 다시 반복

        # 이번회차에 더 교환할 case가 없다면
        ready, change = change, ready           # 다음 번 시행을 위해 ready에 결과값들을 넣어주자

    # cnt만큼 교환이 끝나면
    ans = max(map(int, ready))        # 바꾼 수 중 최댓값 추출
    print('#{} {}'.format(tc, ans))

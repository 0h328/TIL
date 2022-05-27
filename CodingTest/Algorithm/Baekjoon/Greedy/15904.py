import sys
sys.stdin = open('input.txt')

s = input()
alpha_list = ['U', 'C', 'P', 'C']   # UCPC를 찾아야하므로 리스트화

cnt = 0 # UCPC 가 총 4단어이므로 cnt는 4가 되야함.
for i in alpha_list:
    if i in s:      # UCPC 중 알파벳 하나가 s에 포함되면
        cnt += 1    # 개수 체크
        s = s[s.index(i) + 1:]  # 개수를 체크했으므로 포함된 알파벳 제외하고 탐색
    else:           # 포함되지 않으면
        print('I hate UCPC')
        break

if cnt == 4:
    print('I love UCPC')


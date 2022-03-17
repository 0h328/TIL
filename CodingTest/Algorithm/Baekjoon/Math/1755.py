import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())

nums = {'1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
        }

ans = []
for i in range(M, N+1):
    tmp = ' '.join(nums[j] for j in str(i)) # 10이상일 경우, (1,0 / 1,1 / 1,2 ... 으로 str화 시켜서 join함)
    ans.append([i, tmp])        # 숫자와 대응하는 영어를 각각 idx 0과 1의 위치로 ans에 추가

ans.sort(key=lambda x: x[1])    # 영어를 기준으로 정렬

for i in range(len(ans)):
    if i % 10 == 0 and i != 0:  # 10개씩 나눠서 출력
        print()                 # 개행
    print(ans[i][0], end=' ')
import sys
sys.stdin = open('input.txt')


T = int(input())
answer = []

for tc in range(1, T+1):
    N, B = map(int, input().split())        # 점원 수 / 선반 높이
    li = list(map(int, input().split()))    # 점원들 키
    a = 1

    for num in li:
        a |= a << num
    
    idx = 0
    while True:
        if a & 1 << (B + idx):
            answer.append('#{} {}'.format(tc, idx))
            break
        idx += 1

print(*answer, sep='\n')
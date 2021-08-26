import sys
sys.stdin = open('input.txt')
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())                 # N: 화덕 크기 / M: 피자수
    Q = [i for i in range(N)]                        # 화덕
    cheese = list(map(int, input().split()))         # (피자에 처음 뿌려진) 치즈의 양
    temp = N                        # 다음 치즈
    while len(Q) > 1:               # 화덕에 피자가 하나 남을때까지
        i = Q.pop(0)                # 화덕에서 피자를 꺼내고
        cheese[i] //= 2             # 치즈를 녹이고
        if cheese[i] > 0:           # 치즈가 다 녹았는지 확인해서 녹지 않았다면
            Q.append(i)             # 줄어든 치즈를 다시 화덕으로
        elif temp < M:              # 남은 피자의 수가 화덕 크기보다 더 크면 (아직 피자가 남음)
            Q.append(temp)          # 화덕에 피자를 넣고
            temp += 1               # 다음 치즈 확인
    ans = Q[0] + 1                  # 인덱스 + 1 -> 피자 번호
    print('#{} {}'.format(tc, ans))
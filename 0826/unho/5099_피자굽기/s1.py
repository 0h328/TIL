import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    Ci = list(map(list, enumerate(map(int, input().split()), start=1)))     # remain pizza
    oven = [[0, 0]] * N                                                     # 오븐

    idx = 0                                             # 인덱스 번호
    stack = []                                          # 치즈 다 녹은 피자를 순서대로 담을 스택
    while len(stack) != M:                              # 모든 피자가 다 녹을때까지
        if oven[idx % N][1]:                            # 현재 치즈가 남아있으면, 치즈 반 녹음
            oven[idx % N][1] //= 2
            if not oven[idx % N][1]:                    # 녹았는데, 0이 되면 다 녹은 피자 스택에 쌓음
                stack.append(oven[idx % N][0])

        if not oven[idx % N][1] and Ci:                 # 해당 피자의 치즈가 모두 녹아있고, 피자가 더 남아있을때
            oven[idx % N] = Ci.pop(0)                   # 해당 위치에 새로운 피자 추가

        idx += 1

    print('#{} {}'.format(tc, stack.pop()))
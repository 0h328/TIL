import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = input()
    Q = list(map(int, input().split()))
    i = 1

    while True:
        num = Q.pop(0)      # deQueue
        if num - i <= 0:    # 그 값에 i를 뺀 값이 0이하인 경우 -> 숫자가 감소하면서 0보다 작아지는 경우(0포함) -> 0으로 유지되면서 종료(break)
            Q.append(0)     # enQueue
            break           # 종료
        else:               # 0보다 큰 경우는
            num -= i        # num을 i만큼 감소 시키고
        Q.append(num)       # num을 다시 q의 가장 뒤로 이동시키고
        i += 1              # i를 1증가 시키자(다음턴을 위해)
        if i > 5:           # 5 초과 -> 한 사이클(5)을 다 돈 경우
            i = 1           # i를 다시 1로 초기화
    ans = ' '.join(map(str, Q))
    print('#{} {}'.format(tc, ans))
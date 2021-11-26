import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = input()
    l = list(map(int, input().split()))
    i = 0
    while l[i] != 0:            # break 하고나서 조건 확인필요
        for j in range(1, 6):   # 빼주는 값
            x = l[i] - j
            if x <= 0:          # 0보다 작거나 같아진 경우 0으로 변경, break
                l[i] = 0
                break
            else:               # 뺀값으로 l[i]변경 후 i를 변경해서 다음 요소로 넘어감
                l[i] = x
                i = (i+1) % 8

    # 출력
    print('#{} '.format(idx), end=' ')
    for i in range(i-7, i+1):
        print(l[i], end=' ')
    print()


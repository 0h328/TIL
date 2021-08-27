import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    cheeze = []
    for idx, num in enumerate(nums[:N]):
        cheeze.append([num, idx])
    # print(cheeze)

    idx = 0
    while len(cheeze) != 1:  #치즈가 한개 남을 때
        cheeze[0][0] //= 2  # 치즈 반띵
        if cheeze[0][0] == 0: # 치즈가 0인경우
            cheeze.pop(0)
            if N + idx < M:
                cheeze.append([nums[idx + N], idx + N])
                idx += 1
        else:
            cheeze.append(cheeze.pop(0))
    # print(cheeze)
    print('#{} {}'.format(tc+1, cheeze[0][1] + 1))



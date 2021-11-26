import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = []
    i = 0
    while i != 10:
        max_min_num = numbers[0]
        # 최대
        if i % 2 == 0:
            for x in range(len(numbers)):
                if max_min_num < numbers[x]:
                    max_min_num = numbers[x]
            ans.append(max_min_num)
            numbers.remove(max_min_num)
            i += 1
        # 최소
        else:
            for y in range(len(numbers)):
                if max_min_num > numbers[y]:
                    max_min_num = numbers[y]
            ans.append(max_min_num)
            numbers.remove(max_min_num)
            i += 1

    print('#{} {}'.format(tc, ' '.join(list(map(str, ans)))))
import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    size = list(map(int, input().split()))

    weight.sort(reverse=True)
    size.sort(reverse=True)

    total = 0
    for i in range(len(size)):
        for j in range(len(weight)):
            if size[i] >= weight[j]:
                total += weight[j]
                weight = weight[j+1:]
                break
    print('#{} {}'.format(tc+1, total))
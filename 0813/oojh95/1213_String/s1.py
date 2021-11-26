import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    test_case = int(input())
    pattern = input()
    target = input()
    T = len(target)
    P = len(pattern)
    cnt = 0
    for i in range(T - P + 1):
        for j in range(P):
            if target[i + j] != pattern[j]:
                break
        else:
            cnt += 1
    print('#{} {}'.format(test_case, cnt))

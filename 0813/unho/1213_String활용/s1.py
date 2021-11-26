import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())

    answer = 0
    pattern = input()
    in_str = input()

    for i in range(len(in_str) - len(pattern) + 1):
        for j in range(len(pattern)):
            if in_str[i+j] != pattern[j]:
                break
        else:
            answer += 1

    print('#{} {}'.format(tc, answer))
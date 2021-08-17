import sys
sys.stdin = open('input.txt')


def find_palindrome(l):
    max_len = 0
    for sub in [*l, *list(zip(*l))]:
        for i in range(100):  # 시작 index
            for length in range(100 - i, max_len, -1):
                idx = i
                for inter in range(length - 1, -1, -2):
                    if sub[idx] != sub[idx + inter]:
                        break
                    idx += 1
                else:                                       # max_len보다 길이가 긴 회문을 찾은 경우
                    max_len = length
                    # max_len = max(max_len, length)
                    break
    return max_len

for _ in range(10):
    idx = input()
    l = [input() for _ in range(100)]
    print('#{} {}'.format(idx, find_palindrome(l)))
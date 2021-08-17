
import sys

sys.stdin = open('input.txt')


def get_solution(arr, m):
    for word in arr:
        for i in range(100 - m + 1):
            for j in range(m // 2):
                if word[i + j] != word[i + m - 1 - j]:
                    break
            else:
                return m
    return 0


for _ in range(1, 11):

    t = int(input())
    data = [input() for _ in range(100)]
    trans = [''.join(i) for i in zip(*data)]

    max_word = 1
    for i in range(2, 101):
        if i > max_word + 2: break # 회문은 앞 뒤로 두개씩 최대로 들어올 수 있다.
        if max_word < get_solution(data, i): # 회문일 경우만 맥스로 초기화
            max_word = i

    for j in range(max_word + 1, 101):
        if j > max_word + 2: break
        if max_word < get_solution(trans, j):
            max_word = j

    print('#{} {}'.format(_, max_word))

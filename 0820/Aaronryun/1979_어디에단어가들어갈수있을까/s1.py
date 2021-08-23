import sys

sys.stdin = open('input.txt')


def count_one(data):
    cnt_list = []
    for i in data:  # 연속으로 등장하면 하나씩 카운트 하고 카운트 한게 찾고자 하는 숫자면 앤서를 증가시킨다
        cnt = 0

        for j in range(N):
            if i[j] == 1:
                cnt += 1

            else:
                cnt_list.append(cnt) # 어디서 더해줘야 빈칸의 최대길이만 더해줄지를 고민했다.

                cnt = 0
        cnt_list.append(cnt)

    return cnt_list.count(len_word)


for test in range(1, 1 + int(input())):
    N, len_word = list(map(int, input().split()))

    data = [list(map(int, input().split())) for _ in range(N)]
    trans = [i for i in zip(*data)]
    answer = count_one(data) + count_one(trans)

    print('#{} {}'.format(test, answer))

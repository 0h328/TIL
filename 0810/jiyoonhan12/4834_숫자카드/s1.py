import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    num = int(input())
    cardset = str(input())
    cards = [int(cardset[i]) for i in range(num)]

    count = [0] * 10
    for i in range(len(cards)):
        count[cards[i]] += 1

    # print(count)

    max_count = count[0]
    max_num = 0
    for i in range(10):
        if count[i] >= max_count:
            max_count = count[i]
            max_num = i

    print('#{} {} {}'.format(t, max_num, max_count))
import sys
sys.stdin = open('input.txt')

N = int(input())

for num in range(N):
    card_list = list(map(int,input()))

    card_count = [0] * 12

    for card in card_list:
        card_count[card] += 1
    l_index = 0
    tri = run = 0
    while l_index < 10:
        if card_count[l_index] >= 3:
            card_count[l_index] -= 3
            tri += 1
            continue
        if card_count[l_index] >= 1 and card_count[l_index+1] >= 1 and card_count[l_index+2] >= 1:
            card_count[l_index] -= 1
            card_count[l_index+1] -= 1
            card_count[l_index+2] -= 1
            run += 1
            continue
        l_index += 1

    if tri + run == 2:
        print('#{} {}'.format(num + 1, 1))
    else:
        print('#{} {}'.format(num + 1, 0))




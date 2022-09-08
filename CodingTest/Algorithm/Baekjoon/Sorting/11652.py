import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
card_dic = {}

for i in range(N):
    card = int(sys.stdin.readline())
    if card in card_dic:
        card_dic[card] += 1
    else :
        card_dic[card] = 1

res = sorted(card_dic.items(), key=lambda x:(-x[1], x[0]))
print(res[0][0])
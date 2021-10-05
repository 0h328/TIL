import sys
sys.stdin = open('input.txt')

def check_babygin(cards):
    card_list = sorted(cards)
    for i in range(len(card_list)-2):
        temp = card_list[i:i+3]
        avg = sum(temp)/3
        if [avg-1, avg, avg+1]==temp or [avg]*3==temp:
            return True

for T in range(int(input())):
    ckt = 0
    players = [[], []]
    for s in map(int, input().split()):
        idx = ckt%2
        players[idx].append(s)
        if check_babygin(players[idx]):
            ckt = idx+1
            break
        ckt+=1
    else:
        ckt=0
    print('#{} {}'.format((T+1), ckt))

#1 0
#2 1
#3 2
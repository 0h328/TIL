import sys
sys.stdin = open('input.txt')

def solve(player):
    player.sort()
    for i in range(len(player)-2):
        cnt = 1
        if (player[i]+1 in player) and (player[i]+2 in player):
            result = 1
            return result
        if player[i]:
            for j in range(i+1, len(player)):
                if player[i] == player[j]:
                    cnt += 1
            if cnt >= 3:
                result = 1
                return result
    return 0

for tc in range(int(input())):
    card = list(map(int, input().split()))
    first = []
    second = []
    my_list = []
    for i in range(0, 12, 2):
        first.append(card[i])
        second.append(card[i+1])
        if len(first) > 3:
            my_list.append((solve(first), solve(second)))

    final = 0
    for i in range(len(my_list)):
        if my_list[i][0] == my_list[i][1] and my_list[i][0] == 1:
            final = 1
            break
        if my_list[i][0] > my_list[i][1]:
            final = 1
            break
        if my_list[i][0] < my_list[i][1]:
            final = 2
            break
    print('#{} {}'.format(tc+1, final))
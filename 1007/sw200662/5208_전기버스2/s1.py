import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    list_charge = list(map(int, input().split()))
    destination = list_charge[0]
    list_cango = [1]
    ans = -1
    for i in range(1, len(list_charge)):
        list_cango.append(i + list_charge[i])

    while destination != 1:
        for a in range(1, len(list_cango)):
            if list_cango[a] >= destination:
                destination = a
                ans += 1
                break
    print('#{} {}'.format(tc, ans))

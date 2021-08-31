import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N 자격 얻은 사람 수 M 시간당 K 붕어빵 개수
    person = list(map(int, input().split()))
    person.sort()

    bread = [0] * (person[-1]+1)
    customer = [0] * (person[-1]+1)

    # print(len(bread))
    result = True

    for i in range(len(person)):
        customer[person[i]] += 1

    for i in range(1, len(bread)):
        if customer[0] > 0:
            result = False
            break
        if i % M == 0:
            bread[i] += K
        bread[i] += bread[i - 1]
        bread[i] -= customer[i]
        if bread[i] < 0:
            result = False
            break
    if result:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))
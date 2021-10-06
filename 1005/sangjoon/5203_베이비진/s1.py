# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_triplet(cards):
    chk = 0
    cards = cards
    for i in range(10):
        if cards[i] != 0:
            chk += 1
            if chk == 3:
                return True
        else:
            chk = 0

    return False


test_case = int(input())

for test in range(1, test_case + 1):
    lst = list(map(int, input().split()))
    o, t = [0]*10, [0]*10
    ans = 0

    for i, n in enumerate(lst):
        cards = t if i % 2 else o
        cards[n] += 1
        if cards[n] == 3:
            ans = 2 if i % 2 else 1
            break

        if check_triplet(cards):
            ans = 2 if i % 2 else 1
            break

    print("#{} {}".format(test, ans))

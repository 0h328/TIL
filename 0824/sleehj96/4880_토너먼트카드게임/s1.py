import sys
sys.stdin = open('input.txt')


def rps(a, b):
    if (b - a) % 3 == 1:
        return b
    else:
        return a


def divide_group(start, end):

    if start == end:
        return start

    elif end - start == 1:
        winner = rps(card_list[start], card_list[end])
        if card_list[start] == winner:
            return start
        else:
            return end

    else:
        f_s = start
        f_e = (start + end) // 2

        l_s = (start + end) // 2 + 1
        l_e = end

        # former = card_list[f_s:f_e]
        # latter = card_list[l_s:l_e]

        former = divide_group(f_s, f_e)
        latter = divide_group(l_s, l_e)

        winner = rps(card_list[former], card_list[latter])
        if winner == card_list[former]:
            return former
        else:
            return latter


# def divide_group(lst):
#
#     lst_len = len(lst)
#
#     if lst_len == 1:
#         return lst[0]
#
#     elif lst_len == 2:
#         return rps(lst[0], lst[1])
#
#     else:
#         former = lst[:lst_len//2]
#         latter = lst[lst_len//2:]
#         return rps(divide_group(former), divide_group(latter))


T = int(input())
tc = 1
while tc <= T:
    N = int(input())

    card_list = list(map(int, input().split()))
    s = 0
    e = N-1
    ans = divide_group(s, e) + 1

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1

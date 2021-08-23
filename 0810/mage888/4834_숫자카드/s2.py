import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = input()

    n_dict = {}
    for i in range(len(number)):
        n_dict[int(number[i])] = number.count(number[i])
    print(n_dict)

    key_res = 0
    val_res = 0
    for key, val in n_dict.items():
        if key_res < key and val_res < val:
            key_res, val_res = key, val

    print('#{} {} {}'.format(tc, key_res, val_res))


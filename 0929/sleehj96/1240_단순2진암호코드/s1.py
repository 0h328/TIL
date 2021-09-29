import sys
sys.stdin = open('input.txt')


def validation(code: list):
    my_sum = 0
    # odd_sum = 0
    # even_sum = 0
    for idx in range(8):
        if (idx+1) & 1:
            my_sum += code[idx] * 3
            # odd_sum += code[idx]
        else:
            my_sum += code[idx]
            # even_sum += code[idx]
    if my_sum % 10:
        return False
    return True


passcodes = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011',
]

for tc in range(int(input())):
    N, M = map(int, input().split())   # 세로, 가로
    arrays = [input() for _ in range(N)]
    ans = 99999

    for array in arrays:
        arrays_to_check = []
        idx = M-1

        while idx >= 0:
            if array[idx] == '1':
                arrays_to_check.append(array[idx-6:idx+1])
                idx -= 6
            idx -= 1

        passcode = []
        for array_to_check in reversed(arrays_to_check):
            passcode.append(passcodes.index(array_to_check))

        if passcode:
            if validation(passcode):
                t_sum = sum(passcode)
                if ans > t_sum:
                    ans = t_sum

    if ans == 99999:
        ans = 0

    print('#{} {}'.format(tc+1, ans))
    # break

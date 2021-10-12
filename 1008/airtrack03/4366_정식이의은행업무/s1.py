import sys

sys.stdin = open("input.txt")


def check(num_2, num_3):
    result_2 = "".join(num_2)
    result_3 = "".join(num_3)
    if int(result_2, 2) == int(result_3, 3):
        return int("".join(num_2), 2)
    return False


def change(num_2, num_3):
    for i in range(N_2):
        # num_2[i] = "0" if int(num_2[i]) else "1"
        num_2[i] = str(int(num_2[i]) ^ 1)
        for j in range(N_3):
            temp = num_3[j]
            for k in range(3):
                if k != int(temp):
                    num_3[j] = str(k)
                    if check(num_2, num_3):
                        return check(num_2, num_3)
            num_3[j] = temp
        # num_2[i] = "0" if int(num_2[i]) else "1"
        num_2[i] = str(int(num_2[i]) ^ 1)


T = int(input())

for tc in range(1, T + 1):
    num_2 = list(input())
    num_3 = list(input())
    N_2 = len(num_2)
    N_3 = len(num_3)

    ans = change(num_2, num_3)

    print("#{} {}".format(tc, ans))

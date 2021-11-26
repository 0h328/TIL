import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    order, N = input().split()
    my_list = list(input().split())
    s = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    c = [0] * 10

    for i in range(len(my_list)):
        if my_list[i] == s[0]:
            c[0] += 1
        elif my_list[i] == s[1]:
            c[1] += 1
        elif my_list[i] == s[2]:
            c[2] += 1
        elif my_list[i] == s[3]:
            c[3] += 1
        elif my_list[i] == s[4]:
            c[4] += 1
        elif my_list[i] == s[5]:
            c[5] += 1
        elif my_list[i] == s[6]:
            c[6] += 1
        elif my_list[i] == s[7]:
            c[7] += 1
        elif my_list[i] == s[8]:
            c[8] += 1
        else:
            c[9] += 1

    ans = []
    for i in range(10):
        ans += [s[i]] * c[i]

    print('{}'.format(order))
    print(*ans)
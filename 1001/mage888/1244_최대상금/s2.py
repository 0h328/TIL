import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num, s = input().split()    # s : switch
    numbers = set([num])

    for _ in range(int(s)):
        num_switch = set()
        for number in numbers:
            number = list(number)
            for i in range(len(num)-1):
                for j in range(i+1, len(num)):
                    number[i], number[j] = number[j], number[i]
                    num_switch.add(''.join(number))
                    number[i], number[j] = number[j], number[i]
        numbers = num_switch
    print('#{} {}'.format(tc, max(numbers)))
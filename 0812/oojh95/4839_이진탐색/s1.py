import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    start_A = start_B = 1
    end_A = end_B = P
    cnt_A = cnt_B = 0
    while start_A <= end_A:
        middle_A = (start_A + end_A) // 2
        cnt_A += 1
        if A == middle_A:
            break
        elif A > middle_A:
            start_A = middle_A
        else:
            end_A = middle_A
    while start_B <= end_B:
        middle_B = (start_B + end_B) // 2
        cnt_B += 1
        if B == middle_B:
            break
        elif B > middle_B:
            start_B = middle_B
        else:
            end_B = middle_B
    if cnt_A > cnt_B:
        print('#{} B'.format(test_case))
    elif cnt_A == cnt_B:
        print('#{} 0'.format(test_case))
    else:
        print('#{} A'.format(test_case))

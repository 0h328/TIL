import sys
sys.stdin = open('input.txt')

testcase = int(input())
for test in range(testcase):
    total_p, target_a, target_b = map(int, input().split())

    counta = 0
    start_page = 1
    total_page = total_p
    while start_page <= target_a:
        mid_page = int((start_page + total_page) / 2)
        counta += 1
        if mid_page == target_a:
            break
        elif mid_page <= target_a:
            start_page = mid_page
        else:
            total_page = mid_page

    countb = 0
    start_page = 1
    total_page = total_p
    while start_page <= target_b:
        mid_page = int((start_page + total_page) / 2)
        countb += 1
        if mid_page == target_b:
            break
        elif mid_page <= target_b:
            start_page = mid_page
        else:
            total_page = mid_page

    if counta == countb:
        print('#{} 0'.format(test+1))
    elif counta > countb:
        print('#{} {}'.format(test + 1, 'B'))
    elif counta < countb:
        print('#{} {}'.format(test + 1, 'A'))


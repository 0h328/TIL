import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    exam = input()
    list_2 = []
    str_ans = ''

    for z in exam:
        if z == '*':
            list_2.append(z)
        elif z == '+':
            while list_2:
                str_ans += (list_2.pop())
            list_2.append(z)
        else:
            str_ans += z
    while list_2:
        str_ans += list_2.pop()
    print(str_ans)

    result = []
    for z in str_ans:
        if z == '*':
            temp_nums1 = result.pop()
            temp_nums2 = result.pop()
            temp_nums3 = temp_nums1 * temp_nums2
            result.append(temp_nums3)
        elif z == '+':
            temp_nums1 = result.pop()
            temp_nums2 = result.pop()
            temp_nums3 = temp_nums1 + temp_nums2
            result.append(temp_nums3)
        else:
            result.append(int(z))
    print('#{} {}'.format(i+1,result[0]))
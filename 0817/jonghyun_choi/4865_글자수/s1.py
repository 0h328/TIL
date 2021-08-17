import sys
import operator

sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    str1 = input()
    str2 = input()
    count_dict = {}
    for i in str1:
        if i not in count_dict:
            count_dict[i] = str2.count(i)
    sort_dict_value = sorted(count_dict.items(), key=operator.itemgetter(1))[-1][-1]
    print('#{} {}'.format(case + 1, sort_dict_value))

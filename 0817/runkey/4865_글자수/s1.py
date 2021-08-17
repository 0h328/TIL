import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    str1 = input()
    str2 = input()

    cnt_list = []
    for i in str1:
        cnt_list.append(str2.count(i))
    result = max(cnt_list)
    print("#{0} {1}".format(tc, result))
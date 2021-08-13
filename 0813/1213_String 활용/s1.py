import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for i in range(10):
    try_num = int(input())
    find_str = input()
    found_str = input()
    A = len(find_str)
    B = len(found_str)
    cnt = 0
    for z in range(B):
        cnt_test = 0
        for k in range(A):
            if z+k < B:
                if find_str[k] != found_str[z+k]:
                    break
                cnt_test +=1
                if cnt_test == (A):
                    cnt +=1
    print('#{} {}'.format(i+1,cnt))
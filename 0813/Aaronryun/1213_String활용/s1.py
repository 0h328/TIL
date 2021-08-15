import sys

sys.stdin = open('input.txt', encoding='UTF8')

for test in range(10):

    number = input()
    pattern = input()
    target = input()


    print('#{} {}'.format(test+1,target.count(pattern)))
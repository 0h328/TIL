import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    for i in range(len(str2) - len(str1) + 1):
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                break
        else:
            print('#{} 1'.format(test_case))
            break
    else:
        print('#{} 0'.format(test_case))

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    str1_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    str2_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for i in str1:
        str1_dict[i] += 1
    for j in str2:
        if str1_dict[j] != 0:
            str2_dict[j] += 1
    print('#{} {}'.format(test_case, max(str2_dict.values())))


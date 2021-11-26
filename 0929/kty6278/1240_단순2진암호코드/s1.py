import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    code_list = [list(map(str, input().split())) for _ in range(n)]
    num = ['0001101', '0011001', '0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    result = []
    for code in code_list:
        for i in range(len(code)):
            if '1' in code[i]:
                result += code
    result = [*set(result)] # 중복 제거하고 존재하는 연산만 남긴다.
    # print(result)

    bite_num = []
    for bite in result:
        for i in range(len(bite)-1, -1, -1):
            if bite[i] == '1':
                break
        for j in range(i, i-56, -7):
            bite_num.append(bite[j-6:j+1])
    bite_num = bite_num[::-1]
    # print(bite_num)  ['0111011', '0110001', '0111011', '0110001', '0110001', '0001101', '0010011', '0111011']
    for i in range(8): # 값이 8개
        for j in range(10):
            if bite_num[i] == num[j]:
                bite_num[i] = j
    # print(bite_num) [7, 5, 7, 5, 5, 0, 2, 7]
    if ((bite_num[0] + bite_num[2] + bite_num[4] + bite_num[6]) * 3 + bite_num[1] + bite_num[3] + bite_num[5] + bite_num[7]) % 10 == 0:
        total = sum(bite_num)
    else:
        total = 0
    print('#{} {}'.format(tc+1, total))
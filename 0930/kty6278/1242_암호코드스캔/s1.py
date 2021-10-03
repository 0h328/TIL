import sys
sys.stdin = open('input.txt')

#한줄에 암호가 두개 이상인 경우 판단 불가...

for tc in range(int(input())):
    n, m = map(int, input().split())
    code_list = [list(map(str, input().split())) for _ in range(n)]
    num = {'0':'0000','1': '0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

    result = []
    for code in code_list:
        for i in range(len(code)):
            if code[0].isdigit:
                result += code
    result = [*set(result)] # 중복 제거하고 존재하는 연산만 남긴다.
    #print(result)

    bite_num = []
    for bite in result:
        for i in range(len(bite) - 1, -1, -1):
            if bite[i] != '0':
                bite_num.append(bite[0:i + 1])
                break
    #print(bite_num)
    for i in range(len(bite_num)):
        bite_num[i] = bite_num[i].lstrip('0')
    print(bite_num)
    # bite_num = bite_num[::-1]
    temp = ''
    for i in range(len(bite_num)):
        for j in range(len(bite_num[i])):
            temp += num[bite_num[i][j]]
    print(temp)
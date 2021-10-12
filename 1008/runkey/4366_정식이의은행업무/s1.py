import sys
sys.stdin = open('input.txt')
# 제한 시간 초과
for t in range(1, 2):
    tc = int(input())
    result = 0
    num2 = list(input())    # 리스트로 바꿔서 저장
    num3 = list(input())    # 리스트로 바꿔서 저장
    flag = 0
    temp2 = temp3 = 0
    temp2_list = []
    temp3_list = []

    for i in range(len(num2)):
        temp2 = num2.copy()     # 카피
        temp2[i] = str(int(not int(temp2[i])))  # '0'과 '1'이므로 숫자로 변환하여 not을 취해주면
                                                # true, false가 나오고 이를 int취하면 1, 0 => str 변환
        temp2_list.append(''.join(temp2))       # 리스트를 문자로 합침

    for j in range(len(num3)):
        temp3 = num3.copy()     # 카피
        if temp3[j] == '0':     # 해당 자리가 '0'이면
            temp3[j] = '1'      # '1'로 변환한 뒤
            temp3_list.append(''.join(temp3))   # 리스트를 문자로 합침

            temp3[j] = '2'
            temp3_list.append(''.join(temp3))

        elif temp3[j] == '1':
            temp3[j] = '0'
            temp3_list.append(''.join(temp3))

            temp3[j] = '2'
            temp3_list.append(''.join(temp3))

        elif temp3[j] == '2':
            temp3[j] = '0'
            temp3_list.append(''.join(temp3))

            temp3[j] = '1'
            temp3_list.append(''.join(temp3))

    for t2 in temp2_list:
        for t3 in temp3_list:
            if int(t2, 2) == int(t3, 3):    # 문자에 대해서 int(문자,2)를 하면 2진수가 10진수로 변함
                flag = 1                    # 같은 걸 찾으면 탈출
                result = int(t3, 3)         # result에 결과값 담음
                break
        if flag == 1:
            break

    print("#{} {}".format(t, result))
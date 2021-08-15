import sys
sys.stdin = open("input.txt")

test = int(input())                 # test 케이스 갯수
for t in range(1, test + 1):        # test 갯수 만큼 반복
    case = input().split()          # test 번호, 문자 갯수

    result = input().split()        # 문자들을 담음
    temp = []                       # 문자들을 숫자로 변환해서 담음

    for i in range(int(case[1])):   # 각 테스트 케이스 별 갯수만큼 반복
        if result[i] == "ZRO":      # 문자가 ZRO이면
            temp.append(0)          # temp에 0를 삽입
        elif result[i] == "ONE":    # 문자가 ONE이면
            temp.append(1)          # temp에 1를 삽입
        elif result[i] == "TWO":    # 문자가 TWO이면
            temp.append(2)          # temp에 2를 삽입
        elif result[i] == "THR":    # 문자가 THR이면
            temp.append(3)          # temp에 3를 삽입
        elif result[i] == "FOR":    # 문자가 FOR이면
            temp.append(4)          # temp에 4를 삽입
        elif result[i] == "FIV":    # 문자가 FIV이면
            temp.append(5)          # temp에 5를 삽입
        elif result[i] == "SIX":    # 문자가 SIX이면
            temp.append(6)          # temp에 6를 삽입
        elif result[i] == "SVN":    # 문자가 SVN이면
            temp.append(7)          # temp에 7를 삽입
        elif result[i] == "EGT":    # 문자가 EGT이면
            temp.append(8)          # temp에 8를 삽입
        elif result[i] == "NIN":    # 문자가 NIN이면
            temp.append(9)          # temp에 9를 삽입

    temp.sort()                     # temp를 정렬
    result = []                     # result를 초기화

    for i in range(int(case[1])):   # 각 테스트 케이스 별 갯수만큼 반복
        if temp[i] == 0:            # 숫자가 0이면
            result.append("ZRO")    # result에 ZRO를 담음
        elif temp[i] == 1:          # 숫자가 1이면
            result.append("ONE")    # result에 ONE를 담음
        elif temp[i] == 2:          # 숫자가 2이면
            result.append("TWO")    # result에 TWO를 담음
        elif temp[i] == 3:          # 숫자가 3이면
            result.append("THR")    # result에 THR를 담음
        elif temp[i] == 4:          # 숫자가 4이면
            result.append("FOR")    # result에 FOR를 담음
        elif temp[i] == 5:          # 숫자가 5이면
            result.append("FIV")    # result에 FIV를 담음
        elif temp[i] == 6:          # 숫자가 6이면
            result.append("SIX")    # result에 SIX를 담음
        elif temp[i] == 7:          # 숫자가 7이면
            result.append("SVN")    # result에 SVN를 담음
        elif temp[i] == 8:          # 숫자가 8이면
            result.append("EGT")    # result에 EGT를 담음
        elif temp[i] == 9:          # 숫자가 9이면
            result.append("NIN")    # result에 NIN를 담음

    print("#{}".format(t))                              # 현재 테스트 케이스 번호를 출력
    for r in range(len(result)):                        # result의 길이만큼 반복
        if r == len(result)-1:                          # 만약 현재 인덱스가 result길이의 -1과 같으면
           print("{}".format(result[r]))                # result[r]을 출력 후 줄바꿈
        else:                                           # 현재 인덱스가 마지막 인덱스가 아니면
           print("{}".format(result[r]), end=" ")       # 공백을 사이에 두고 result[r]을 출력

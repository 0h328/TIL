import sys
sys.stdin = open('input.txt')

# 미완성

pattern = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

def hex_To_binary(arr):
    arr = arr.replace('0', '0000')
    arr = arr.replace('1', '0001')
    arr = arr.replace('2', '0010')
    arr = arr.replace('3', '0011')
    arr = arr.replace('4', '0100')
    arr = arr.replace('5', '0101')
    arr = arr.replace('6', '0110')
    arr = arr.replace('7', '0111')
    arr = arr.replace('8', '1000')
    arr = arr.replace('9', '1001')
    arr = arr.replace('A', '1010')
    arr = arr.replace('B', '1011')
    arr = arr.replace('C', '1100')
    arr = arr.replace('D', '1101')
    arr = arr.replace('E', '1110')
    arr = arr.replace('F', '1111')

    return arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 입력받은 암호를 2진수로 변환
    for i in range(8):
        arr[i] = hex_To_binary(arr[i])

    sumV = 0
    for row in range(1, N):
        # row의 열이 전부0으로 구성된 경우
        if arr[row].find('1') < 0:
            continue

        # 각 row 암호코드의 오른쪽 끝 찾기 위해
        col = M*4 - 1
        while col > 56:
            if arr[row][col] == '1' and arr[row-1][col] == '0':
                res = []
                for _ in range(8):
                    cnt1 = cnt2 = cnt3 = 0
                    while arr[row][col] == '1':
                        cnt1 += 1
                        col -= 1
                    while arr[row][col] == '0':
                        cnt2 += 1
                        col -= 1
                    while arr[row][col] == '1':
                        cnt3 += 1
                        col -= 1
                    # 0에 대한 col위치 이동
                    while col >= 0 and arr[row][col] == '0':
                        col -= 1

                    r = min(cnt1, cnt2, cnt3)
                    # cnt1, cnt2, cnt3와 r을 사용하여 숫자를 pattern에서 찾아서 res에 추가
                    tnum = pattern.index(cnt3//r*100 + cnt2//r*10 + cnt1//r)
                    res.insert(0, tnum)
                # print(res)

                # res를 검증
                oddV = res[0] + res[2] + res[4] + res[6]
                evenV = res[1] + res[3] + res[5] + res[7]
                if (oddV*3 + evenV) % 10 == 0:
                    sumV += sum(res)

            else:
                col -= 1

    print('#{} {}'.format(tc, sumV))
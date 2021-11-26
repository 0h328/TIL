import sys
sys.stdin = open('input.txt')

def binarySearch(start, end, cnt, value):
    if start > end:
        return 1001                                              # 답을 못 찾는 경우 최대값 반환
    div = (start+end)//2
    if div == value:                                             # 답을 찾은 경우
        return cnt
    else:                                                        # 못 찾은 경우
        if div > value:                                          # div가 더 큰 경우(end를 div로 줄임)
            return binarySearch(start, div, cnt + 1, value)
        else:                                                    # div가 작은 경우(start를 div로 높임)
            return binarySearch(div, end, cnt+1, value)

T = int(input())
for test in range(T):
    page, A, B = map(int, input().split())
    find_A = binarySearch(1, page, 0, A)
    find_B = binarySearch(1, page, 0, B)

    if find_A > find_B:
        print('#{} {}'.format(test+1, 'B'))
    elif find_A < find_B:
        print('#{} {}'.format(test+1, 'A'))
    else:
        print('#{} {}'.format(test+1, '0'))
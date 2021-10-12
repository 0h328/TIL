import sys
import math
sys.stdin = open('input.txt')

def exch(n, type):
    num = ''
    while n>0:
        n, mod = divmod(n, type)
        num = str(mod) + num
    return num
def exch_list(n, type):
    num = []
    while n > 0:
        n, mod = divmod(n, type)
        num.insert(0, mod)
    return num
def list_to_10num(nums, type):#리스트로 되어있는 거 십진수로 바꿔주는 거
    ans = 0
    for i in range(len(nums)):
        ans += nums[-1-i]*pow(type, i)
    return ans

T = int(input())

for tc in range(1, T+1):
    binum = input()
    thrnum = input()
    binum_10 = int(binum, 2)
    thrnum_10 = int(thrnum, 3)
    thrnum_3 = exch(thrnum_10, 3)

    # print(exch(18, 2))
    # print(exch(18,3))


    thrnum_3_list_origin = exch_list(thrnum_10, 3)
    thrnum_3_list = exch_list(thrnum_10, 3)
    pow2_list = []
    for n in range(len(binum)):
        pow2_list.append(pow(2,n))

    minu = 0
    for idx in range(len(thrnum_3_list)):
        for j in range(3):
            thrnum_3_list[idx] = j
            if thrnum_3_list == exch_list(thrnum_10, 3):
                continue
            else:
                new_thrnum_3to10 = list_to_10num(thrnum_3_list, 3)
                minu = new_thrnum_3to10-binum_10

                if not new_thrnum_3to10:
                    break
                if abs(minu) in pow2_list and minu < 0 and binum[-int(math.log2(abs(minu)))-1]=='1':
                    # print(thrnum_3_list)
                    # print(minu, math.log2(abs(minu)))
                    # print(binum[-int(math.log2(abs(minu)))])
                    print('#{} {}'.format(tc, new_thrnum_3to10))
                    # print('-')
                elif minu in pow2_list and binum[-int(math.log2(abs(minu)))-1]=='0':
                    # print(thrnum_3_list)
                    print('#{} {}'.format(tc, new_thrnum_3to10))
                    # print('+')
        thrnum_3_list = exch_list(thrnum_10, 3)
        # print(thrnum_3_list)


    # print(thrnum_3)
    # print(thrnum_3_list)

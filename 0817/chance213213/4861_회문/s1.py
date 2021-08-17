import sys
sys.stdin=open('input.txt')

N = int(input())
#SOLVE PLAN
#arr에 extend를 이용하여 문자 하나씩 list에 추가함
#그러면 100개의 요소를 가진 리스트가 생성 될 것이고, %10을 이용해서, 풀어야지
#여기서 회문 찾고, 역으로 만드는 것도 해야지


def samereverse(arr):
    for i in range(10):
        cnt = 0
        for idx in range(5):
            if arr[idx + i * 10] == arr[9 - idx + i * 10]:
                cnt += 1
                if cnt == 5:
                    ans = arr[i * 10: i*10 + 9]
                    return ans
            else:
                break

    return 0

def samereverse2(arr):
    for i in range(10):
        cnt = 0
        for idx in range(5):
            if arr[i+idx*10] == arr[90-idx*10+i]:
                cnt += 1
                if cnt == 5:
                    ans = arr[i::10]
                    return ''.join(ans)
            else:
                break


for tc in range(1, N+1):
    A, B = map(int, input().split())
    arr = []
    for i in range(10):
        arr.append(list(input()))
    print(arr)
    # print(samereverse(arr))
    # print(samereverse2(arr))
    #회문 판별은 쉬움, //2한 idx 값 끼리 비교!


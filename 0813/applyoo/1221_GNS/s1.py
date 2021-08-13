import sys
sys.stdin = open('input.txt', encoding='UTF8')

def gns(arr):
    result = []
    # 딕셔너리 item 0으로 초기화
    other_number = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}

    for i in arr: # arr의 요소와 같은 해당 key의 item +1
        other_number[i] += 1

    for i in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]: # 순서대로 리스트 반복
        result.extend([i]*other_number[i]) # 딕셔너리의 item 값 만큼 리스트인 i를 곱하여 정렬된 리스트 생성

    return result

T = int(input())
for _ in range(T):
    test, num = map(str, input().split())
    arr = list(map(str, input().split()))
    result = gns(arr)
    print(test)
    print(*result)
import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N = int(input())
    boxes = list(map(int, input().split()))
    # 최대 낙차 저장
    result = 0
    # 마지막 -1 까지만 돈다.
    for i in range(len(boxes)-1):
        # 현재 index에서 최대 낙차
        max_gravity = N-(i+1)
        # 현재 result보다 작으면 더이상 판단할 필요없음
        if max_gravity < result:
            break

        # 다음 열 박스들 체크
        for j in range(i+1, len(boxes)):
            # 다음 박스가 크거나 같으면 낙차거리가 1씩 줄어듬
            if boxes[i] <= boxes[j]:
                max_gravity-=1
                # 위와 마찬가지로 현재 result보다 작으면 판단중지
                if max_gravity < result:
                    break
        # 만약 정상적으로 전부 돌았다면, result를 더 큰 값으로 변경 
        # (사실 그냥 result = max_gravity로 해도 상관없을 듯)
        else:
            result = max(result, max_gravity)
    
    # 현재 테스트케이스의 결과 출력
    print(result)

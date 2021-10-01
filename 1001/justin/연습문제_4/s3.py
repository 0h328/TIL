"""
연습문제 3. 순열

3-3) 5개의 숫자 중 3자리의 순열 생성하기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""

def perm(n, k, m):                                # n: 숫자를 결정 할 자리 인덱스, k: 순열의 길이, m: 주어진 숫자의 개수
    if n == k:                                    # 결정이 끝나면
        for i in range(k):                        # 혹은 print(*nums[:3])
            print(nums[i], end=' ')
        print()
    else:
                                                  # 자기 자신부터 마지막(m-1)까지 진행
        for i in range(n, m):                     # n번과 바꿀 위치
            nums[n], nums[i] = nums[i], nums[n]   # 위치 교환
            perm(n+1, k, m)                       # n+1(다음 요소 결정)
            nums[n], nums[i] = nums[i], nums[n]   # 이전 단계를 위한 원상 복구

nums = [1, 2, 3, 4, 5]
perm(0, 3, 5)
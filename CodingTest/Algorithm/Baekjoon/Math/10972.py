import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):     # 마지막 항부터 돈다
    if arr[i-1] < arr[i]:       # 만약 앞 열의 값이 그 뒷열의 값보다 작다면
        for j in range(N-1, 0, -1):     # 다시 그 앞 열의 값을 맨 뒷열부터 비교
            if arr[i-1] < arr[j]:       # 그 앞열의 값이 뒤에 있는 어느 열보다 작다면
                arr[i-1], arr[j] = arr[j], arr[i - 1]   # 그 두 값을 스왑
                arr = arr[:i] + sorted(arr[i:])         # i-1 번째 까지의 리스트와 그 뒤에리스트를 정렬한 채로 붙인다.
                print(*arr)     # *를 이용해 리스트 내부의 원소들을 공백을 사용하여 출력
                exit()          # 코드 종료

print(-1)  # 만약 위에서 코드 종료가 일어나지 않았다면(마지막 항이라면) -1 출력
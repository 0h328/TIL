import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    nums = input()
    after_nums = '' # 후위표현식으로서 저장할 변수
    stack_gae = [] # 괄호,곱,플러스등을 일시적으로 저장해둘 리스트
    for k in nums:
        if k.isdigit(): # 숫자라면 그대로 후위표현식에 저장
            after_nums += k
        elif k == ')': # 닫는괄호가 나왓다면
            while stack_gae and stack_gae[-1] != '(': # 여는괄호가 나올때까지, 그리고 stack이 존재할때까지
                after_nums += stack_gae.pop()
            stack_gae.pop() # < 여는 괄호가 나왔다면, 제거

        elif k == '+': # 플러스 기호가 나왔다면
            while stack_gae and stack_gae[-1] != '(': # 플러스가 나왓다면, 모두다 꺼내주는데 여는괄호가 나온다면 멈춰줌
                after_nums += stack_gae.pop()
            stack_gae.append(k) # 그다음 플러스를 더해줌
        else:
            stack_gae.append(k)
    result = []
    for z in after_nums:
        if z == '*':
            temp_nums1 = result.pop()
            temp_nums2 = result.pop()
            temp_nums3 = temp_nums1 * temp_nums2
            result.append(temp_nums3)
        elif z == '+':
            temp_nums1 = result.pop()
            temp_nums2 = result.pop()
            temp_nums3 = temp_nums1 + temp_nums2
            result.append(temp_nums3)
        else:
            result.append(int(z))
    print('#{} {}'.format(i+1,result[0]))
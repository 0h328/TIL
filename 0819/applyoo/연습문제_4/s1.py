# 디버거를 통해 결과를 확인해보세요
# print 결과는 디버거를 실행 시켰을 때 보이는 'Console'이라는 탭에서 확인 가능합니다.

def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('메인시작')
func1()
print('메인끝')

"""
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수 1 종료
메인끝
"""
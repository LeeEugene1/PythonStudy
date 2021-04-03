##함수 선언부분
def myFunc():
    print('함수를 호출함.')

#전역변수 선언
gVar = 100

#메인코드부분
if __name__ == '__main__' :
    print('메인함수 실행')
    myFunc()
    print('전역변수:',gVar)

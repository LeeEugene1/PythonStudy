# a = b = 10 = c = d = 20
# print(b)

#8진수 17을 10진수로 변환
# print(int('17',8))

# print(int('1002',2)) 2진수에서 0,1만 가능
# print(int('1008', 8))
# print(int('FFAG',16)) 16진수에서 F까지만 가능

# print(bin(12))
# print(hex(12))
# print(oct(12))

#16진수 글자 하나를 입력하면 16진수인지 아닌지를 구분하는 코드를 작성하시오
num16 = input('진수 한글자 입력:')
if '0' <= num16 <= '9' or 'A' <= num16 <='F':
    print("10진수->", int(num16,16))
else:
    print('16진수가 아닙니다.')

#파이썬에서 제공되는 각 데이터형의 기본크기를 확인하는 프로그램을 만들어보자
import sys

if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

print('int형 기본크기->', sys.getsizeof(intVar))
print('float형 기본크기->', sys.getsizeof(floatVar))
print('bool형 기본크기->', sys.getsizeof(boolVar))
print('str형 기본크기->', sys.getsizeof(strVar))
print('list형 기본크기->', sys.getsizeof(strVar))
print('tuple형 기본크기->', sys.getsizeof(tupleVar))
print('dictionary형 기본크기->', sys.getsizeof(dictVar))
print('set형 기본크기->', sys.getsizeof(setVar))

#문자열을 입력받고 거꾸로 출력해보자 예) Python -> nohtyP
inStr = input('문자열을 입력--->')

for i in range(len(inStr)-1,-1,-1):
    print('%c' % inStr[i], end='')
print('%d' % 100)
print('100+100')

#100 / 200 = 0
print('%d / %d = %d' % (100,200,0.5))

#100 / 200 = 0.500000
print('%d / %d = %f' % (100,200,0.5))

#100 / 200 = 0.5
print('%d / %d = %5.1f' % (100,200,0.5))

#정수형 데이터의 서식 지정
print('%d' % 123)
print('%5d' % 123)
print('%05d' % 123)

#실수형 데이터의 서식지정
print('%f' % 123.45)
print('%7.1f' % 123.45)
print('%7.3f' % 123.45)

#문자열 데이터의 서식지정
print('%s' % 'python')
print('%10s' % 'python')

#format() 함수와 {}를 함께사용해 서식을 지정할 수도 있다.
print('%d %5d %05d' % (123,123,123))
print('{0:d} {1:5d} {2:05d}'.format(123,123,123))

#format()함수는 출력순서를 지정할 수 있어서 좋다
print('{1:d} {0:d} {2:d}'.format(100,200,300))

#이스케이프 문자
print('한 행입니다 \n또 한행입니다')
print('\t탭키\t연습')
print('글자가 \"강조\"되는 효과1')
print('글자가 \'강조\'되는 효과2')
print('\\\\\\ 역슬래시 3개출력')
print(r'\n \t \' \\를 그대로 출력')

#변수의 선언과 사용
boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""

print(type(boolVar), type(intVar), type(floatVar), type(strVar))

#숫자 147출력
print(0b10010011)
print(int('10010011',2))
print(int('93',16))
print(0x93)

sel = int(input('입력 진수 결정(16/10/8/2):'))
num = input('값 입력:')

if sel != 16 and sel != 10 and sel != 8 and sel != 2:
    print('16,10,8,2숫자중 하나만 입력하세요')
if sel == 16:
    num10 = int(num,16)
if sel == 10:
    num10 = int(num,10)
if sel == 8:
    num10 = int(num,8)
if sel == 2:
    num10 = int(num,2)


print('16진수 ->',hex(num10))
print('10진수 ->',num10)
print('8진수 ->',oct(num10))
print('2진수 ->',bin(num10))

a = 100 ** 100
print(a)



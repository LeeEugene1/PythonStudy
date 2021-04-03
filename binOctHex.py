#파이썬 진수변환 함수
#bin() : 2진수, oct() : 8진수, hex() : 16진수

sel = int(input('입력 진수 결정(16/10/8/2)'))
num = input('값 입력:')

num10 = 0
if sel == 16:
    num10 = int(num, 16)
elif sel == 10:
    num10 = int(num, 10)
elif sel == 8:
    num10 = int(num,8)
elif sel == 2:
    num10 = int(num,2)
else:
    print('16,19,8,2 숫자중 하나만 입력하세요')
    exit()


print('16진수->',hex(num10))
print('10진수->',num10)
print('8진수->',oct(num10))
print('2진수->',bin(num10))
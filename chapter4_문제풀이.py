#윤년계산

year = int(input('연도입력:'))
if (year % 4 == 0) and (year % 100 != 0) :
    print(year,'년은 윤년입니다')
elif (year % 400 == 0):
    print(year, '년은 윤년입니다')
else:
    print(year,'년은 윤년이 아닙니다')
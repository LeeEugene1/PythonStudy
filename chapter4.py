#동전교환프로그램

money,c50000,c10000,c5000,c1000 = 0,0,0,0,0

money = int(input('교환할 돈은 얼마?'))

c50000 = money // 50000
money = money % 50000

c10000 = money // 10000
money = money % 10000

c5000 = money // 5000
money = money % 5000

c1000 = money // 1000
money = money % 1000

print('50000원짜리 ->',c50000)
print('10000원짜리 ->',c10000)
print('5000원짜리 ->',c5000)
print('1000원짜리 ->',c1000)

print('바꾸지못한 잔돈->',money)
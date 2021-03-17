python = "Python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())#파이썬첫글자가 대문자냐? True
print(len(python))#length
print(python.replace('Python','JAVA'))#단어찾고 바꾸기

print(python.count('n'))#n이 몇번등장하는지 세기

#어떤문자가 어느위치index에 있는지
index = python.index('n')
print(index) #5
#앞에찾은 인덱스 그 다음
index = python.index('n', index+1)
print(index) #17

print(python.find('n')) #5

#find와 index의 차이
print(python.find('cat')) #없으므로 -1 계속 프로그램 진행
print('hi')
print(python.index('cat'))#에러를 내면서 프로그램 종료해버림 그다음문장을 진행하지못함
print('hi')
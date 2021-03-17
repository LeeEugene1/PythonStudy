#소휴식 고양이를 소개해주세요~
animal = 'cat'
name = '골목대장'
age = 4
hobby = '낮잠'
is_adult = age >= 3

print("소휴식"+animal+"의 이름은"+name+"이에요")
print(name + '은' + str(age)+'살이며, ' + hobby +'을 아주좋아해요')
print(name + '은 어른일까요?' + str(is_adult))
#정수 age, boolean is_adult는 문자열로 바꾸어서 출력해야하므로 str에 감싸준다.

hobby = '구경하기'
#변수이기때문에 값을 변경가능

# + 대신에 ,를 사용하면 정수형,boolean을 그대로쓸수있어서 str()로 안감싸도됨
print(name,'은', age,'살이며 취미는',hobby,'에요. 어른일까요?',is_adult)

#전체주석처리 ctrl+/
'''이렇게하면
여러줄이
주석처리됩니다'''

#Quiz1)변수를 이용하여 다음문장 출력(변수명: station, 변수값:"사당", '신도림', '인천공항' | 출력문장 : 'xx행 열차가 들어오고있습니다')
station = '사당'
print(station,'행 열차가 들어오고 있습니다.')
station = '신도림'
print(station,'행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station,'행 열차가 들어오고 있습니다.')

#문자열은 ''과 "", '''가있다
sentence = """여러줄이
가능한
문자열"""
print(sentence)
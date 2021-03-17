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

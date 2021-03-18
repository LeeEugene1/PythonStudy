class Car():#붕어빵찍는틀 ()안에는 object생략
    maxSpeed = 300
    maxPeople = 5
    def start(self):
        print('출발')
    def stop(self):
        print('정지')
    def __str__(self):
        return 'hello world'
    def __init__(self):
        print('인스턴스가 만들어졌습니다!!!!!')#인스턴스가 만들어질때마다 무조건생성 2~3


#class는 붕어빵 찍는 툴로 생각한다면 instance는 붕어빵(찍혀서나온것)이다.
#k9 = Car()#찍혀서나온것, k3, k5등등
#print(k9.maxPeople)#찍혀서나온것

#아래처럼 클래스는 직접만지지않는다.
# print(Car.maxPeople)

#print(type(k9))
#print(dir(k9))

#상속
class Hybrid(Car):
    battery = 1000
    betteryKM = 300

k9 = Car()
k3 = Hybrid()
print(k9.maxPeople) #5
print(k3.maxPeople) #5
print(type(k9)) #클래스
print(dir(k9)) 
print(k9) #인스턴스를 출력할때마다 설정한 문구들이 나온다

#그밖에 built-in function도 많으니 공부하자
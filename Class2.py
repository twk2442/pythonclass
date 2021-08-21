#생성자 
#생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다
#상속
#보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
#"클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?" 
# 라는 의문이 들 수도 있다. 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 
# 상속을 사용해야 한다.

class FourCal:
    def __init__(self,first,second):  #class 내부에 구현된 함수를 메소드라고 부른다
        self.first = first            #__init__라는 메소드 이름을 쓰면 파이썬이 자동으로 
        self.second = second          #생성자(constructor)라고 인식한다
    def add(self):
        result = self.first + self.second  #메소드 
        return result
    def mul(self):
        result = self.first * self.second   #메소드
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a=FourCal(4,2)

print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b=MoreFourCal(4,3)
print(b.pow())
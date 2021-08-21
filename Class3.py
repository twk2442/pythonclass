#매서드 오버라이딩
#SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성하였다. 
# 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 
# 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

#class 변수
#클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.


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







class SafeFourCal(FourCal):
    name ='jina'
    def div(self):
        if self.second == 0:
            return 0
        else :
            return self.first/self.second

a =SafeFourCal(4,0)

print(a.div())
print(a.name)
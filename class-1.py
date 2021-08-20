#class  사칙연산 class 작성

class FourCal:
    def setdata(self,first,second):  #class 내부에 구현된 함수를 메소드라고 부른다
        self.first = first
        self.second = second
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

a = FourCal()   #a는 FourCal class의 객체 
a.setdata(4,2)

#클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

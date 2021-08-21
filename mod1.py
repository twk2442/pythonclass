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
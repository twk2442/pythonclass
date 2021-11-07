#생활코딩 함수수업 
print('hello world')
print(3)
print(len('hello world'))

#len ,print 같은 기본제공함수는 내장함수 / 수많은 내장함수 존재한다
#함수 왜 쓸까?: 코드를 간단하게 줄여주고 , 재사용가능, 유지보수 쉽게,--> 가독성 up

def get_vat():   # def 함수이름():~~~~~
    price=1000   # 함수의 기능 :1 서로비슷한 것들 모아놓은것    
    vat_rate=0.1
    print(price*vat_rate)

get_vat()

def get_vat1(price):   # price 매개변수 
    vat_rate=0.1
    print(price*vat_rate)

get_vat1(10000)   #숫자 10000 인자 
get_vat1(20000)

def get_vat2(price,vat_rate):
    print(price*vat_rate)

get_vat2(100,2)
get_vat2(200,3)

def get_vat3(price,vat_rate=0.1):  # 매개변수에 지정하면 입력 안 할 시 기본값으로 설정 
    print(price*vat_rate)

get_vat3(10)

def get_vatf(price,vat_rate=0.1):
    return price*vat_rate 

print(get_vatf(200))          




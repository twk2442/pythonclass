#string 데이터 타입,연산

#'로시작하면'로끝 "로시작하면 "로 끝 둘다 동일의미
print('hello world')
print("hello world")
 
# 장문의 string데이터 입력시 ''' 나 """사용 
print(''' 
hello
world
''')

#string 연산, 함수 

print("'1'+'1'",'1'+'1')  #"" 안에 ' '를 써도 상관 없음 " "안에는 다 string취급 
print("hello world"*1000)
print("'hello world'* 1000",len("hello world"*1000))
print("replace func",'hello world'.replace('world','python'))



#함수 :반복적으로 사용되는 가치있는 부분을 한 뭉치로 
# 묶어서 만든것


def add(a,b):   #여기서 a,b를 매개변수라고 부름 
    return a+b

a=3
b=4
c=add(a,b)   
print(c)


print(add(3,5))  #여기서 3,5를 인수라고 부른다

 
def say(name, old ,man=True):  #이렇게 매개변수 초깃값 설정해놓으려면 매개변수 맨 마지막에다가 놓아야 한다
     print("나의이름은 %s입니다." % name)
     print("나이는 %d살입니다." %old)
     if man :
         print("상남자")
     else:
         print("천상여자")

say('jina',24,man=False)





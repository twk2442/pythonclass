#함수안에서 함수밖 변수 변경


def vr(a):
    a=a+1
    return a


a=1
a=vr(a)
print(a)


#람다

add=lambda a,b:a+b
result =add(2,3)
print(result)
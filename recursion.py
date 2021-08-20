#함수 사용하여 간단한recursion 작성


#n 부터 0까지의 합
def func(num):
    if num == 0 :
        return 0 
    else :
        return num+func(num-1)


result = func(4)

print(result)

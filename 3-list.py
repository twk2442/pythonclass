#list :서로연관된 데이터타입을 모아서 정리해주는 data type
#list는 통계에서 많이 사용된다.
import statistics #통계관련된 모듈
import random

#리스트 정의
student =['tw','j-a','sj']
salary = [1,4,7]

print(student)
print(student[1])

#리스트 함수적용

i = statistics.mean(salary)  #평균값 구해주는 함수
print(i)

s = random.choice(student)  #아무나 한명 뽑아주는 함수
print(s)


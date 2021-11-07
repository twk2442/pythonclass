#서로 연관된 코드를 모아서 이름을 붙인 파일을 모듈이라고 합니다. 
#서로 연관된 모듈을 모아서 이름을 붙인 디렉토리를 패키지라고 합니다. 


import arithmethic
import statistic
import num.arithmethic
import num.statistic    # import 패키지이름.모듈 으로 선언
#관습적으로 맨 위에다가 씀
#모듈내의 함수를 사용하려면 import로 선언해야한다


print(arithmethic.sum(1,2))
print(statistic.sum(1,2))

#from statistic import sum
#print(sum(1,3))

from statistic import sum as ssum # ssum으로 이름 변경 
print(ssum(1,3))

#패키지 모듈 사용

print(num.arithmethic.sum(1,4))
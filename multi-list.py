#다중 리스트 

name, address, interest = ['sj', 'seoul', 'game']   # 변수 여러개 선언하는것이 인덱스 대신  // 장점:인덱스 사용할 때 보다 좀더 데이터의 의미파악이 좋다 
print(name, address, interest)

persons = [['sj', 'seoul','game'],['tw','ilsan','sports'],['ja','seoul','tv']]

for name,address,interest in persons :  # for 구문에서도 변수 여러개 사용가능
    print(name ,address , interest )
